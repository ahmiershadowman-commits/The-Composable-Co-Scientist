"""Tests for the RETRIEVE primitive."""
from compositional_co_scientist.core.primitives.retrieve import retrieve


def test_retrieve_fetches_documents():
    """Test that retrieve fetches documents from sources with relevance scoring."""
    results = retrieve(
        query="superconductivity mechanisms",
        sources=["arxiv", "wikipedia"],
        relevance_threshold=0.5
    )
    assert len(results["results"]) >= 1
    assert "relevance_scores" in results
