from langchain.text_splitter import CharacterTextSplitter
from langchain_core.documents import Document


# TODO: Add model and embedding model choices from user
# TODO: Add model and embedding model choices from application settings
class DocumentManager:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 0):
        self._chunk_size = chunk_size
        self._chunk_overlap = chunk_overlap
        pass

    def from_text(self, text: str, metadata: dict = {}) -> list[Document]:
        text_splitter = CharacterTextSplitter(
            chunk_size=self._chunk_size,
            chunk_overlap=self._chunk_overlap,
        )
        documents = [
            Document(page_content=page) for page in text_splitter.split_text(text)
        ]
        documents = self._attach_metadata_to_documents(documents, metadata)

        return documents

    def _attach_metadata_to_documents(
        self, documents: list[Document], metadata: dict
    ) -> list[Document]:
        for doc in documents:
            doc.metadata = metadata
        return documents
