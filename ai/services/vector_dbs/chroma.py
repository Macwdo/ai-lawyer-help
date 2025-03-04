# from chromadb.config import Settings
# from langchain_chroma import Chroma
# from langchain_community.vectorstores import Chroma
# from langchain_core.documents import Document
# from langchain_core.embeddings import Embeddings


# class ChromaService:
#     def __init__(self, embeddings: Embeddings):
#         self._settings = Settings()
#         self.chroma = Chroma(embedding_function=embeddings)

#     def upload_documents(self, documents: list[Document]):
#         self.chroma.from_documents(documents)
