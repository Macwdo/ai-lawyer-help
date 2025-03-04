from django.conf import settings
from langchain_core.embeddings import Embeddings
from langchain_postgres import PGVector


class PostgresVectorDB:
    def __init__(self, *, embeddings: Embeddings):
        self._embeddings = embeddings
        self._conn_str = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
            settings.POSTGRES_USER,
            settings.POSTGRES_PASSWORD,
            settings.POSTGRES_HOST,
            settings.POSTGRES_PORT,
            settings.POSTGRES_DB_NAME,
        )

    def __call__(self, *args, **kwds):
        return self._get_connection()

    def _get_connection(self) -> PGVector:
        return PGVector(embeddings=self._embeddings, connection=self._conn_str)
