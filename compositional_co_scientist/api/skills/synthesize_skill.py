"""Synthesize skill wrapper for the SYNTHESIZE primitive.

Use when synthesizing surviving candidates into a coherent output.
Triggers the SYNTHESIZE primitive (P7).
"""
from typing import Dict, Any
import json

from compositional_co_scientist.core.primitives.synthesize import synthesize as synthesize_primitive
from compositional_co_scientist.core.models.candidate import Candidate
from compositional_co_scientist.core.models.document import Document


SYNTHESIZE_PROMPT = """Synthesize the following surviving candidates into a coherent output.

**Surviving Candidates:**
{survivors}

**Context/Documents:**
{context}

**Instructions:**
1. Integrate the key insights from all surviving candidates
2. Preserve tensions and disagreements - do NOT smooth over important differences
3. Produce a coherent, well-structured output
4. Note any unresolved tensions or open questions
5. Provide a confidence score (0.0-1.0) for the synthesis

**Output format:**
```json
{{
  "output": "The synthesized output text",
  "tensions": [
    {{"aspect": "What the tension is about", "positions": ["View A", "View B"], "resolution": "How resolved or 'unresolved'"}}
  ],
  "confidence": 0.8,
  "justification": "Why this confidence level"
}}
```
"""


def _parse_llm_response(response_text: str) -> Dict[str, Any]:
    """Parse LLM response into synthesis result.
    
    Args:
        response_text: Raw text from LLM
        
    Returns:
        Dictionary with output, tension_map, confidence
    """
    try:
        # Try to extract JSON from response
        if "```json" in response_text:
            json_str = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            json_str = response_text.split("```")[1].split("```")[0].strip()
        else:
            json_str = response_text.strip()
        
        data = json.loads(json_str)
        
        # Convert tensions list to tension_map dict
        tension_map = {}
        for tension in data.get("tensions", []):
            aspect = tension.get("aspect", "unknown")
            tension_map[aspect] = {
                "positions": tension.get("positions", []),
                "resolution": tension.get("resolution", "unresolved")
            }
        
        return {
            "output": data.get("output", response_text),
            "tension_map": tension_map,
            "confidence": data.get("confidence", 0.5)
        }
    except (json.JSONDecodeError, KeyError):
        # Fallback: return raw text as output
        return {
            "output": response_text,
            "tension_map": {},
            "confidence": 0.5
        }


def synthesize(survivors: Dict[str, Any], context: Dict[str, Any] = None, 
               preserve_tensions: bool = True, llm_response: str = None) -> Dict[str, Any]:
    """Synthesize survivors into coherent output.

    Args:
        survivors: SurvivorSet from SELECT primitive containing:
            - survivors: List of selected candidate dictionaries
            - similarity_matrix: Dictionary mapping candidate pairs to similarity scores
        context: ContextSet from RETRIEVE primitive containing:
            - results: List of retrieved document dictionaries
        preserve_tensions: Whether to preserve disagreements between candidates.
        llm_response: Optional pre-computed LLM response (for testing/host integration).

    Returns:
        Dictionary containing:
            - output: Synthesized output string
            - tension_map: Dictionary mapping tensions between candidates
            - confidence: Confidence score for the synthesis (0.0-1.0)
    """
    if context is None:
        context = {}

    # Format survivors for prompt
    survivors_text = "\n".join([
        f"**Candidate {c.get('id', i+1)}:** {c.get('content', 'No content')}"
        for i, c in enumerate(survivors.get("survivors", []))
    ])
    
    # Format context for prompt
    context_text = "\n".join([
        f"**Document {d.get('id', i+1)}** (source: {d.get('source', 'unknown')}, relevance: {d.get('relevance_score', 0.5)}):\n{d.get('content', 'No content')}"
        for i, d in enumerate(context.get("results", []))
    ]) if context.get("results") else "No additional context provided."

    # If LLM response provided (from host), parse it
    if llm_response:
        result = _parse_llm_response(llm_response)
    else:
        # Use primitive's placeholder synthesis
        survivor_candidates = [
            Candidate(
                id=c.get("id", f"c{i}"),
                goal_id=c.get("goal_id", "unknown"),
                content=c.get("content", ""),
                metadata=c.get("metadata", {})
            )
            for i, c in enumerate(survivors.get("survivors", []))
        ]

        survivors_obj = {"survivors": survivor_candidates, "similarity_matrix": survivors.get("similarity_matrix", {})}

        context_docs = [
            Document(
                id=d.get("id", f"d{i}"),
                source=d.get("source", "unknown"),
                content=d.get("content", ""),
                metadata=d.get("metadata", {}),
                relevance_score=d.get("relevance_score", 1.0)
            )
            for i, d in enumerate(context.get("results", []))
        ]

        context_obj = {"results": context_docs}

        result = synthesize_primitive(survivors_obj, context_obj, preserve_tensions)

    return {
        "output": result["output"],
        "tension_map": result["tension_map"],
        "confidence": result["confidence"],
        "prompt_used": SYNTHESIZE_PROMPT.format(
            survivors=survivors_text,
            context=context_text
        ),
        "preserve_tensions": preserve_tensions
    }
