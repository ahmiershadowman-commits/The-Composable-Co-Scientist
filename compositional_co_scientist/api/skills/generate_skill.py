"""Generate skill wrapper for the GENERATE primitive.

Use when generating candidate hypotheses or solutions for a research goal or question.
Triggers the GENERATE primitive (P1) to produce diverse candidates.
"""
from typing import Dict, Any
import uuid
import json

from compositional_co_scientist.core.primitives.generate import generate as generate_primitive
from compositional_co_scientist.core.models.candidate import Candidate


GENERATE_PROMPT = """Generate {max_candidates} diverse candidate hypotheses for the following research goal:

**Goal:** {goal}

**Constraints:**
{constraints}

**Instructions:**
1. Each hypothesis should be novel and testable
2. Hypotheses should be mutually distinct (avoid mode collapse)
3. Include a brief rationale for each hypothesis
4. Format as JSON array with "content" and "rationale" fields

**Output format:**
```json
[
  {{"content": "Hypothesis 1", "rationale": "Why this might be true"}},
  {{"content": "Hypothesis 2", "rationale": "Why this might be true"}}
]
```
"""


def _parse_llm_response(response_text: str, goal: str, temperature: float) -> list:
    """Parse LLM response into Candidate objects.
    
    Args:
        response_text: Raw text from LLM
        goal: Research goal these candidates address
        temperature: Temperature used for generation
        
    Returns:
        List of Candidate objects
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
        
        candidates = []
        for item in data:
            candidate = Candidate(
                id=str(uuid.uuid4()),
                goal_id=goal[:50],
                content=item.get("content", str(item)),
                metadata={
                    "temperature": temperature,
                    "rationale": item.get("rationale", "")
                }
            )
            candidates.append(candidate)
        
        return candidates
    except (json.JSONDecodeError, KeyError, IndexError):
        # Fallback: create simple candidates from text
        lines = [l.strip() for l in response_text.strip().split('\n') if l.strip()]
        return [
            Candidate(
                id=str(uuid.uuid4()),
                goal_id=goal[:50],
                content=line,
                metadata={"temperature": temperature, "parsed": True}
            )
            for line in lines[:5]
        ]


def generate(goal: str, constraints: Dict[str, Any] = None, temperature: float = 0.7, 
             llm_response: str = None) -> Dict[str, Any]:
    """Generate candidate hypotheses for a given goal.

    Args:
        goal: The research goal or question to generate hypotheses for.
        constraints: Constraints for generation (e.g., max_candidates).
        temperature: Temperature parameter for generation diversity (0.0-1.0).
        llm_response: Optional pre-computed LLM response (for testing/host integration).
                     If not provided, uses placeholder generation.

    Returns:
        Dictionary containing:
            - candidates: List of generated Candidate objects
            - diversity_score: Score indicating diversity among candidates (0.0-1.0)
    """
    if constraints is None:
        constraints = {}
    
    max_candidates = constraints.get("max_candidates", 5)

    # If LLM response provided (from host), parse it
    if llm_response:
        candidates = _parse_llm_response(llm_response, goal, temperature)
    else:
        # Use primitive's placeholder generation
        result = generate_primitive(goal, constraints, temperature)
        candidates = result["candidates"]

    # Convert candidates to serializable format
    candidates_data = [
        {
            "id": c.id,
            "goal_id": c.goal_id,
            "content": c.content,
            "metadata": c.metadata,
            "created_at": c.created_at.isoformat()
        }
        for c in candidates
    ]

    # Compute diversity (placeholder - will be enhanced with sentence-transformers)
    diversity_score = 0.5 if len(candidates) < 2 else 0.7

    return {
        "candidates": candidates_data,
        "diversity_score": diversity_score,
        "prompt_used": GENERATE_PROMPT.format(
            max_candidates=max_candidates,
            goal=goal,
            constraints=json.dumps(constraints, indent=2)
        )
    }
