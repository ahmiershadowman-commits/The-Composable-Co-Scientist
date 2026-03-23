"""SELECT primitive for survivor selection with diversity enforcement.

This primitive selects surviving candidates from a scored set while enforcing
diversity quotas to prevent premature convergence in the search space.
"""
from typing import Dict, Any, List
from compositional_co_scientist.core.models.candidate import Candidate
from compositional_co_scientist.core.models.score import Score


def select(scored: Dict[str, Any], diversity_quota: float = 0.4) -> Dict[str, Any]:
    """Select surviving candidates from a scored set with diversity enforcement.

    Args:
        scored: Dictionary containing:
            - scores: List of Score objects from EVALUATE primitive
            - candidates: List of Candidate objects to select from
        diversity_quota: Fraction of top candidates to select (0.0-1.0).
                        Default 0.4 selects top 40% of candidates.

    Returns:
        Dictionary containing:
            - survivors: List of selected Candidate objects
            - similarity_matrix: Dictionary mapping candidate pairs to similarity scores
    """
    scores = scored.get("scores", [])
    candidates = scored.get("candidates", [])
    
    # Handle empty input
    if not scores or not candidates:
        return {"survivors": [], "similarity_matrix": {}}
    
    # Create candidate lookup by ID
    candidate_map = {c.id: c for c in candidates}
    
    # Sort scores by score value (descending)
    sorted_scores = sorted(scores, key=lambda s: s.score, reverse=True)
    
    # Calculate number of survivors based on diversity quota
    num_survivors = max(1, int(len(sorted_scores) * diversity_quota))
    
    # Select top candidates
    selected_scores = sorted_scores[:num_survivors]
    survivors = [candidate_map[s.candidate_id] for s in selected_scores if s.candidate_id in candidate_map]
    
    # Compute similarity matrix for survivors
    similarity_matrix = compute_similarity_matrix(survivors)
    
    return {"survivors": survivors, "similarity_matrix": similarity_matrix}


def compute_similarity_matrix(candidates: List[Candidate]) -> Dict[str, Dict[str, float]]:
    """Compute pairwise similarity matrix among candidates.

    Uses Jaccard similarity on token sets as the default algorithm.
    For production use, this can be enhanced with sentence-transformers
    embeddings (see spec Section 2.1).

    Args:
        candidates: List of Candidate objects to compute similarities for.

    Returns:
        Nested dictionary mapping candidate_id -> {other_id: similarity_score}
        where similarity_score is between 0.0 (no similarity) and 1.0 (identical).
    """
    if len(candidates) < 2:
        return {}
    
    # Tokenize candidates
    def tokenize(text: str) -> set:
        """Tokenize text into a set of lowercase words."""
        return set(text.lower().split())
    
    candidate_tokens = {c.id: tokenize(c.content) for c in candidates}
    
    # Compute Jaccard similarity for all pairs
    similarity_matrix = {}
    for i, c1 in enumerate(candidates):
        similarity_matrix[c1.id] = {}
        for j, c2 in enumerate(candidates):
            if i == j:
                similarity_matrix[c1.id][c2.id] = 1.0
            elif c2.id in similarity_matrix and c1.id in similarity_matrix[c2.id]:
                # Use already computed value (symmetric)
                similarity_matrix[c1.id][c2.id] = similarity_matrix[c2.id][c1.id]
            else:
                # Compute Jaccard similarity
                tokens1 = candidate_tokens[c1.id]
                tokens2 = candidate_tokens[c2.id]
                intersection = len(tokens1 & tokens2)
                union = len(tokens1 | tokens2)
                similarity = intersection / union if union > 0 else 0.0
                similarity_matrix[c1.id][c2.id] = similarity
    
    return similarity_matrix
