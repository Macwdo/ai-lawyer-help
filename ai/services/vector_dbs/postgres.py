from django.conf import settings
from langchain_core.embeddings import Embeddings
from langchain_postgres import PGVector


class PostgresVectorDB:
    def __init__(self, *, embeddings: Embeddings):
        self._embeddings = embeddings
        self.__db_settings = settings.DATABASES["default"]
        self._conn_str = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
            self.__db_settings["USER"],
            self.__db_settings["PASSWORD"],
            self.__db_settings["HOST"],
            self.__db_settings["PORT"],
            self.__db_settings["NAME"],
        )

    def __call__(self, *args, **kwds):
        return self._get_connection()

    def _get_connection(self) -> PGVector:
        return PGVector(embeddings=self._embeddings, connection=self._conn_str)
