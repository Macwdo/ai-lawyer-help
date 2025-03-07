from ai.services.ai.ai_service import AiService
from common import constants


class ImageToTextService(AiService):
    def __init__(self):
        pass

    # TODO: Implement Dynamic model in a feature
    def get_model(self):
        from django.conf import settings
        from langchain_ollama import OllamaLLM
        from langchain_openai import ChatOpenAI

        if settings.OCR_MODEL == constants.LLAVA_7B_MODEL:
            return OllamaLLM(model=constants.LLAVA_7B_MODEL)

        elif settings.OCR_MODEL == constants.OPENAI_GPT_4_O_MODEL:
            return ChatOpenAI(model=constants.OPENAI_GPT_4_O_MODEL)
        # TODO: Improve error handling
        raise ValueError("Invalid OCR model")

    def process(self, *, image_path: str) -> str:
        pass
