import os
from qdrant_client import QdrantClient

class QdrantIntegration:
    def __init__(self, host='localhost', port=6333):
        self.client = QdrantClient(host=host, port=port)

    def create_collection(self, collection_name, vector_size):
        self.client.recreate_collection(
            collection_name=collection_name,
            vector_size=vector_size
        )

    def insert_vectors(self, collection_name, vectors, payloads=None):
        self.client.upload_collection(
            collection_name=collection_name,
            vectors=vectors,
            payload=payloads
        )

    def search_vectors(self, collection_name, query_vector, top_k=5):
        return self.client.search(
            collection_name=collection_name,
            query_vector=query_vector,
            top=top_k
        )

# Example usage
if __name__ == "__main__":
    qdrant = QdrantIntegration()
    qdrant.create_collection("example_collection", vector_size=128)
    qdrant.insert_vectors("example_collection", vectors=[[0.1] * 128])
    results = qdrant.search_vectors("example_collection", query_vector=[0.1] * 128)
    print(results)
