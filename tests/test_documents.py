from app.document_loader import load_documents,chunk_documents
def test_documents_load_and_chunk():
 docs=load_documents("data"); chunks=chunk_documents(docs)
 assert len(docs)==6 and chunks
 assert all(c["metadata"]["chunk_id"]==c["id"] for c in chunks)
