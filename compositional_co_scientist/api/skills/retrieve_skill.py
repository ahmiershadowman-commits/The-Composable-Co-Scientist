"""Retrieve skill wrapper for the RETRIEVE primitive.

Use when retrieving relevant documents from sources for a research query.
Triggers the RETRIEVE primitive (P5).
"""
from typing import Dict, Any, List

from compositional_co_scientist.core.primitives.retrieve import retrieve as retrieve_primitive
from compositional_co_scientist.core.models.document import Document


def retrieve(query: str, sources: List[str] = None, relevance_threshold: float = 0.5) -> Dict[str, Any]:
    """Retrieve documents from specified sources for a given query.

    Args:
        query: The search query to retrieve documents for.
        sources: List of sources to search (e.g., 'arxiv', 'wikipedia', 'pubmed').
        relevance_threshold: Minimum relevance score for documents to be included.

    Returns:
        Dictionary containing:
            - results: List of retrieved Document objects
            - relevance_scores: Dictionary mapping document IDs to relevance scores
    """
    if sources is None:
        sources = ["arxiv", "wikipedia", "pubmed"]

    result = retrieve_primitive(query, sources, relevance_threshold)

    # Convert results to serializable format
    results_data = [
        {
            "id": doc.id,
            "source": doc.source,
            "content": doc.content,
            "metadata": doc.metadata,
            "relevance_score": doc.relevance_score,
            "created_at": doc.created_at.isoformat()
        }
        for doc in result["results"]
    ]

    return {
        "results": results_data,
        "relevance_scores": result["relevance_scores"]
    }
