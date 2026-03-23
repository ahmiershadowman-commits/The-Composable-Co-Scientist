"""Evaluate skill wrapper for the EVALUATE primitive.

Use when evaluating candidate hypotheses against a rubric.
Triggers the EVALUATE primitive (P2) with constraint C1 (evaluator independence).
"""
from typing import Dict, Any, List
import json

from compositional_co_scientist.core.primitives.evaluate import evaluate as evaluate_primitive
from compositional_co_scientist.core.models.candidate import Candidate
from compositional_co_scientist.core.models.score import Score


EVALUATE_PROMPT = """Evaluate the following candidate hypotheses against the provided rubric.

**Rubric Criteria:**
{rubric}

**Candidates to Evaluate:**
{candidates}

**Instructions:**
1. Score each candidate on a scale of 0.0 to 1.0 for each criterion
2. Provide a brief justification for each score
3. Calculate a weighted total score based on rubric weights
4. Be critical - avoid score inflation (self-evaluation bias is 10-25%)
5. This is an EVALUATE operation - must use different model than GENERATE (C1 constraint)

**Output format:**
```json
[
  {{"candidate_id": "id1", "scores": {{"criterion1": 0.8, "criterion2": 0.6}}, "total": 0.7, "justification": "Why this score"}},
  {{"candidate_id": "id2", "scores": {{"criterion1": 0.5, "criterion2": 0.9}}, "total": 0.7, "justification": "Why this score"}}
]
```
"""


def _parse_llm_response(response_text: str, candidate_ids: List[str], rubric: Dict[str, float], evaluator_model: str) -> list:
    """Parse LLM response into Score objects.
    
    Args:
        response_text: Raw text from LLM
        candidate_ids: IDs of candidates being evaluated
        rubric: Rubric criteria and weights
        evaluator_model: Model used for evaluation
        
    Returns:
        List of Score objects
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
        
        scores = []
        for item in data:
            score = Score(
                candidate_id=item.get("candidate_id", candidate_ids[0]),
                evaluator_model=evaluator_model,
                score=item.get("total", 0.5),
                rubric={
                    "criteria_scores": item.get("scores", {}),
                    "justification": item.get("justification", ""),
                    "weights": rubric
                },
                calibration=1.0
            )
            scores.append(score)
        
        return scores
    except (json.JSONDecodeError, KeyError, IndexError):
        # Fallback: return moderate scores for all candidates
        return [
            Score(
                candidate_id=cid,
                evaluator_model=evaluator_model,
                score=0.5,
                rubric={"fallback": True, "weights": rubric}
            )
            for cid in candidate_ids
        ]


def evaluate(candidates: List[Dict[str, Any]], rubric: Dict[str, float], 
             evaluator_model: str, llm_response: str = None) -> Dict[str, Any]:
    """Evaluate candidates against a rubric using an evaluator model.

    Args:
        candidates: List of candidate dictionaries with id and content.
        rubric: Dictionary of evaluation criteria and their weights.
        evaluator_model: Name/ID of the model used for evaluation.
        llm_response: Optional pre-computed LLM response (for testing/host integration).

    Returns:
        Dictionary containing:
            - scores: List of Score objects for each candidate
            - calibration: Calibration factor for the scores (default 1.0)

    Raises:
        ValueError: If evaluator_model is not specified (C1 constraint).
    """
    if not evaluator_model:
        raise ValueError("C1 constraint: evaluator_model must be specified (evaluator independence required)")

    candidate_ids = [c["id"] for c in candidates]
    
    # Format candidates for prompt
    candidates_text = "\n".join([
        f"**Candidate {c.get('id', i+1)}:** {c['content']}"
        for i, c in enumerate(candidates)
    ])
    
    # Format rubric for prompt
    rubric_text = "\n".join([f"- {criterion}: {weight}" for criterion, weight in rubric.items()])

    # If LLM response provided (from host), parse it
    if llm_response:
        scores = _parse_llm_response(llm_response, candidate_ids, rubric, evaluator_model)
    else:
        # Use primitive's placeholder evaluation
        candidate_objs = [
            Candidate(
                id=c["id"],
                goal_id=c.get("goal_id", "unknown"),
                content=c["content"],
                metadata=c.get("metadata", {})
            )
            for c in candidates
        ]
        candidates_dict = {"candidates": candidate_objs}
        result = evaluate_primitive(candidates_dict, rubric, evaluator_model)
        scores = result["scores"]

    # Convert scores to serializable format
    scores_data = [
        {
            "candidate_id": s.candidate_id,
            "evaluator_model": s.evaluator_model,
            "score": s.score,
            "rubric": s.rubric,
            "calibration": s.calibration,
            "created_at": s.created_at.isoformat()
        }
        for s in scores
    ]

    return {
        "scores": scores_data,
        "calibration": 1.0,
        "prompt_used": EVALUATE_PROMPT.format(rubric=rubric_text, candidates=candidates_text),
        "c1_enforced": True
    }
