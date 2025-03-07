from abc import ABC, abstractmethod

from langchain_core.language_models import BaseLLM


class AiService(ABC):
    """
    All AI services should implement this interface.
    We wanna have control of how model are being set up.


    """

    @abstractmethod
    def get_model(self) -> BaseLLM:
        pass
