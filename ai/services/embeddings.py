from uuid import uuid4

from django.conf import settings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

from ai.services.vector_dbs.postgres import PostgresVectorDB


# TODO: Add model and embedding model choices from user
# TODO: Add model and embedding model choices from application settings
class EmbeddingManager:
    def __init__(self, model_name: str = "text-embedding-3-small"):
        self._model_name = model_name
        self._embedding_model = OpenAIEmbeddings(
            api_key=settings.OPENAI_API_KEY,
            model=self._model_name,
        )
        self._vector_db = PostgresVectorDB(embeddings=self._embedding_model)()

    def store_embeddings(self, documents: list[Document]):
        self._assign_ids_to_documents(documents)
        self._vector_db.add_documents(documents)

    def process_documents(
        self,
        file_path: str,
        chunk_size: int = 1000,
        chunk_overlap: int = 0,
        metadata: dict = {},
    ) -> list[Document]:
        metadata = metadata or {}
        documents = TextLoader(file_path).load()
        documents = self._attach_metadata_to_documents(documents, metadata)
        return CharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        ).split_documents(documents)

    def _assign_ids_to_documents(self, documents: list[Document]):
        for doc in documents:
            doc.id = str(uuid4())

    def _attach_metadata_to_documents(
        self, documents: list[Document], metadata: dict
    ) -> list[Document]:
        for doc in documents:
            doc.metadata = metadata
        return documents

    def get_embedding_model(self):
        return self._embedding_model
