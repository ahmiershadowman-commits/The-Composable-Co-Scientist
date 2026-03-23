"""C3 constraint: Diversity Quota enforcement.

This constraint enforces a minimum diversity threshold at SELECT to prevent
premature convergence on similar candidates.
"""
from typing import Dict, Any
from compositional_co_scientist.core.errors import ConstraintViolationError


# Default thresholds (configurable)
DEFAULT_MAX_SIMILARITY = 0.7  # Candidates above this are "too similar"
DEFAULT_MIN_DIVERSITY = 0.4   # Minimum acceptable diversity score


def check_diversity_quota(
    similarity_matrix: Dict[str, Dict[str, float]],
    max_similarity: float = DEFAULT_MAX_SIMILARITY
) -> Dict[str, Any]:
    """Check C3: Diversity quota at SELECT.

    Args:
        similarity_matrix: Dictionary mapping candidate pairs to similarity scores.
        max_similarity: Maximum acceptable similarity between any pair (default 0.7).

    Returns:
        Dictionary containing:
            - passed: True if constraint satisfied
            - max_found: Maximum similarity found in matrix
            - violating_pairs: List of candidate pairs exceeding threshold

    Raises:
        ConstraintViolationError: If diversity quota not met.
    """
    if not similarity_matrix:
        # Empty matrix = single candidate or none, pass by default
        return {"passed": True, "max_found": 0.0, "violating_pairs": []}

    violating_pairs = []
    max_found = 0.0

    for c1_id, similarities in similarity_matrix.items():
        for c2_id, sim in similarities.items():
            if c1_id != c2_id:  # Skip self-similarity
                max_found = max(max_found, sim)
                if sim > max_similarity:
                    violating_pairs.append((c1_id, c2_id, sim))

    if violating_pairs:
        raise ConstraintViolationError(
            f"C3 violated: {len(violating_pairs)} pair(s) exceed similarity threshold "
            f"{max_similarity}. Max similarity found: {max_found:.3f}. "
            f"Violating pairs: {[(p[0][:8], p[1][:8], f'{p[2]:.3f}') for p in violating_pairs[:5]]}"
        )

    return {"passed": True, "max_found": max_found, "violating_pairs": []}


def check_diversity_score(
    diversity_score: float,
    min_diversity: float = DEFAULT_MIN_DIVERSITY
) -> bool:
    """Check if diversity score meets minimum threshold.

    Args:
        diversity_score: Computed diversity score (0.0-1.0).
        min_diversity: Minimum acceptable diversity (default 0.4).

    Returns:
        True if diversity quota met.

    Raises:
        ConstraintViolationError: If diversity below threshold.
    """
    if diversity_score < min_diversity:
        raise ConstraintViolationError(
            f"C3 violated: Diversity score {diversity_score:.3f} below minimum "
            f"{min_diversity}. Regenerate with anti-canon prompt."
        )
    return True


def generate_anti_canon_prompt(original_goal: str) -> str:
    """Generate an anti-canon prompt for regeneration.

    Used when C3 violation triggers regeneration. Forces divergence from
    canonical/obvious answers.

    Args:
        original_goal: The original research goal.

    Returns:
        Modified prompt that encourages non-canonical responses.
    """
    return f"""{original_goal}

**ANTI-CANON CONSTRAINT:**
Generate hypotheses that deliberately diverge from obvious/canonical answers.
Avoid the most commonly cited explanations in the literature.
Prioritize novel mechanisms, unconventional frameworks, or cross-domain analogies.

**Diversity Requirement:**
Each hypothesis must be meaningfully distinct from others (no rephrasing)."""
