from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

from app.config import ai_settings


class ChromaStore:

    def __init__(self):

        self.client = PersistentClient(
            path=ai_settings.CHROMA_DB_PATH
        )

        self.collection = self.client.get_or_create_collection(
            name="farming_memory"
        )

        self.embedding_model = SentenceTransformer(
            ai_settings.EMBEDDING_MODEL
        )

    def embed(self, text):

        return self.embedding_model.encode(
            text
        ).tolist()

    def add_case(
        self,
        case_id,
        document,
        metadata
    ):

        embedding = self.embed(
            document
        )

        self.collection.add(

            ids=[case_id],

            documents=[document],

            embeddings=[embedding],

            metadatas=[metadata]

        )

    def search(
        self,
        query,
        top_k=3
    ):

        embedding = self.embed(
            query
        )

        results = self.collection.query(

            query_embeddings=[embedding],

            n_results=top_k

        )

        return results

    def count(self):

        return self.collection.count()


chroma_store = ChromaStore()