from django.db import models as m
from langchain_core.language_models import BaseLLM


class LLMModels(m.TextChoices):
    pass


class OpenAIModels(LLMModels):
    OPENAI_TRANSCRIPT_MODEL = "whisper-1"
    OPENAI_GPT_4_O_MODEL = "gpt-4o"
    OPENAI_GPT_4_O_MINI_MODEL = "gpt-4o-mini"
    OPENAI_TTS_MODEL = "tts-1"


class OllamaModels(LLMModels):
    LLAVA_7B_MODEL = "llava:7b"  # OCR

    DEEPSEEK_CODER_V2_16B = "deepseek-coder-v2:16b"

    DEEPSEEK_R1_14B = "deepseek-r1:14b"
    DEEPSEEK_R1_8B = "deepseek-r1:8b"
    DEEPSEEK_R1_1_5B = "deepseek-r1:1.5b"

    LLAMA3_1_8B = "llama3.1:8b"

    GEMMA3_27B = "gemma3:27b"  # OCR
    GEMMA3_12B = "gemma3:12b"  # OCR
    GEMMA3_4B = "gemma3:4b"  # OCR


class LLMService:
    def __init__(self):
        pass

    def _get_ocr_models(self):
        return [
            OllamaModels.LLAVA_7B_MODEL,
            OpenAIModels.OPENAI_GPT_4_O_MODEL,
            OllamaModels.GEMMA3_27B,
            OllamaModels.GEMMA3_12B,
            OllamaModels.GEMMA3_4B,
        ]

    def get_llm(
        self,
        *,
        model: OpenAIModels | OllamaModels = OllamaModels.GEMMA3_12B,
    ) -> BaseLLM:
        from langchain_ollama import OllamaLLM
        from langchain_openai import OpenAI

        if isinstance(model, OllamaModels):
            return OllamaLLM(model=model)

        if isinstance(model, OpenAIModels):
            return OpenAI()

    def get_ocr_llm(
        self,
        *,
        model: OpenAIModels | OllamaModels = OllamaModels.GEMMA3_12B,
    ) -> BaseLLM:
        if model not in self._get_ocr_models():
            raise ValueError(f"Invalid model: {model}")

        return self.get_llm(model=model)

    def get_reasoning_llm(
        self,
        *,
        model: OllamaModels = OllamaModels.GEMMA3_12B,
    ) -> BaseLLM:
        return self.get_llm(model=model)
