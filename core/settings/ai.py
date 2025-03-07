from os import getenv

# WARN: For development porpuses, we want to use local models for development.
# If i can't use local models, i will use openai models.

OCR_MODEL = getenv("OCR_MODEL", "llava:7b")
TRANSCRIPT_MODEL = getenv("TRANSCRIPT_MODEL", "whisper-1")
LLM_MODEL = getenv("LLM_MODEL", "llava:7b")
