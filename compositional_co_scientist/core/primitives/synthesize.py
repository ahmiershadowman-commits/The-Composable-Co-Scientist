"""SYNTHESIZE primitive for composing final output from survivors and context.

This primitive synthesizes a final output from survivor candidates and retrieved
context, optionally preserving tensions between competing perspectives.
"""
from typing import Dict, Any


def synthesize(survivors: Dict[str, Any], context: Dict[str, Any], 
               preserve_tensions: bool = True) -> Dict[str, Any]:
    """Synthesize final output from survivors and context.

    Args:
        survivors: Dictionary containing survivor candidates from SELECT primitive.
                   Expected keys:
                   - survivors: List of Candidate objects that survived selection
        context: Dictionary containing retrieved context from RETRIEVE primitive.
                 Expected keys:
                 - results: List of Document objects from retrieval
        preserve_tensions: If True, maintain and report tensions between
                          competing perspectives in the output. Default True.

    Returns:
        Dictionary containing:
            - output: Synthesized text output combining survivors and context
            - tension_map: Dictionary mapping tension identifiers to descriptions
                          (empty if preserve_tensions=False)
            - confidence: Float between 0.0 and 1.0 indicating confidence in output
    """
    # Extract survivors list
    survivors_list = survivors.get("survivors", [])
    
    # Extract context results
    context_results = context.get("results", [])
    
    # Initialize tension map
    tension_map = {}
    
    # Compute confidence based on available evidence
    # Higher confidence with more survivors and context
    survivor_count = len(survivors_list)
    context_count = len(context_results)
    
    # Simple confidence heuristic: based on evidence availability
    if survivor_count == 0 and context_count == 0:
        confidence = 0.5  # Baseline confidence with no evidence
    else:
        # Confidence increases with evidence, capped at 0.95
        evidence_score = min(1.0, (survivor_count + context_count) / 10.0)
        confidence = 0.5 + (0.45 * evidence_score)
    
    # If preserve_tensions is True and we have multiple survivors,
    # identify tensions between them
    if preserve_tensions and survivor_count > 1:
        tension_map = _identify_tensions(survivors_list)
    
    # Generate synthesized output
    output = _generate_output(survivors_list, context_results, tension_map)
    
    return {
        "output": output,
        "tension_map": tension_map,
        "confidence": round(confidence, 2)
    }


def _identify_tensions(survivors: list) -> Dict[str, str]:
    """Identify tensions between multiple survivor candidates.

    Args:
        survivors: List of Candidate objects to analyze for tensions.

    Returns:
        Dictionary mapping tension identifiers to descriptions of the
        competing perspectives or contradictions.
    """
    tensions = {}
    
    # Simple tension detection: look for contrasting content
    # In production, this would use NLP to detect contradictions
    for i, s1 in enumerate(survivors):
        for j, s2 in enumerate(survivors[i+1:], i+1):
            # Create tension identifier
            tension_id = f"tension_{s1.id}_{s2.id}"
            
            # Simple heuristic: different content suggests tension
            if s1.content != s2.content:
                tensions[tension_id] = (
                    f"Perspective divergence between {s1.id} and {s2.id}"
                )
    
    return tensions


def _generate_output(survivors: list, context: list, tension_map: dict) -> str:
    """Generate synthesized output text.

    Args:
        survivors: List of Candidate objects to synthesize.
        context: List of Document objects providing context.
        tension_map: Dictionary of tensions to preserve in output.

    Returns:
        Synthesized text output.
    """
    parts = []
    
    # Add survivor content
    if survivors:
        parts.append("## Key Findings")
        for survivor in survivors:
            parts.append(f"- {survivor.content}")
    
    # Add context
    if context:
        parts.append("\n## Supporting Evidence")
        for doc in context:
            parts.append(f"- From {doc.source}: {doc.content[:100]}...")
    
    # Add tensions if present
    if tension_map:
        parts.append("\n## Alternative Perspectives")
        for tension_id, description in tension_map.items():
            parts.append(f"- {description}")
    
    if not parts:
        return "No content available for synthesis."
    
    return "\n".join(parts)
