from app.vector_db.embeddings import EmbeddingGenerator
from app.vector_db.store_manager import store_manager

def test_embedding_generation():
    emb = EmbeddingGenerator().embed("hello world")
    assert emb is not None
    assert len(emb.shape) == 1

def test_faiss_add_and_search():
    store_manager.add_text("this is a test vector")
    dist, idx = store_manager.search("test query", k=1)
    assert len(dist) == 1
    assert len(idx) == 1
