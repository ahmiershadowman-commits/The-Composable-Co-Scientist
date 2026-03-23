"""SELECT primitive for survivor selection with diversity enforcement.

This primitive selects surviving candidates from a scored set while enforcing
diversity quotas to prevent premature convergence in the search space.
"""
from typing import Dict, Any, List, Optional
from compositional_co_scientist.core.models.candidate import Candidate
from compositional_co_scientist.core.models.score import Score

# Global cache for sentence-transformers model
_embedding_model = None


def _get_embedding_model():
    """Lazy-load sentence-transformers model."""
    global _embedding_model
    if _embedding_model is None:
        try:
            from sentence_transformers import SentenceTransformer
            _embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        except ImportError:
            _embedding_model = None  # Fall back to Jaccard
    return _embedding_model


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

    Uses sentence-transformers embeddings with cosine similarity when available.
    Falls back to Jaccard similarity on token sets if embeddings unavailable.

    Args:
        candidates: List of Candidate objects to compute similarities for.

    Returns:
        Nested dictionary mapping candidate_id -> {other_id: similarity_score}
        where similarity_score is between 0.0 (no similarity) and 1.0 (identical).
    """
    if len(candidates) < 2:
        return {}

    # Try sentence-transformers first
    model = _get_embedding_model()
    if model is not None:
        return _compute_similarity_with_embeddings(model, candidates)
    
    # Fall back to Jaccard similarity
    return _compute_similarity_jaccard(candidates)


def _compute_similarity_with_embeddings(model, candidates: List[Candidate]) -> Dict[str, Dict[str, float]]:
    """Compute similarity using sentence-transformers embeddings.
    
    Args:
        model: SentenceTransformer model
        candidates: List of Candidate objects
        
    Returns:
        Similarity matrix using cosine similarity
    """
    from sentence_transformers.util import cos_sim
    import torch
    
    # Get embeddings for all candidates
    texts = [c.content for c in candidates]
    embeddings = model.encode(texts, convert_to_tensor=True)
    
    # Compute cosine similarity matrix
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
                # Compute cosine similarity
                sim = cos_sim(embeddings[i].unsqueeze(0), embeddings[j].unsqueeze(0))
                similarity_matrix[c1.id][c2.id] = float(sim[0][0])
    
    return similarity_matrix


def _compute_similarity_jaccard(candidates: List[Candidate]) -> Dict[str, Dict[str, float]]:
    """Compute similarity using Jaccard similarity on token sets.
    
    Args:
        candidates: List of Candidate objects
        
    Returns:
        Similarity matrix using Jaccard similarity
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
