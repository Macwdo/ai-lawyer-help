from langchain_core.messages import HumanMessage
from pydantic import BaseModel

from ai.services.ai.llm import LLMService


class ResumeImageResult(BaseModel):
    content: str
    score: float


class ImageManager:
    def __init__(self):
        self._ocr_llm = LLMService().get_ocr_llm()
        self._llm = LLMService().get_llm()

    def resume_image(self, path: str):
        prompt_path = "ai/services/prompts/resume_image.txt"
        prompt = open(prompt_path, "r").read()

        message = HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": prompt,
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": path,
                    },
                },
            ]
        )

        return self._ocr_llm.invoke([message])

    def generate_image_title_from_resume(self, resume: str):
        prompt = f"""
        The resume provived is from an image extracted from a PDF.
        
        I want to generate an image title based on the image resume.
        The image resume is the following:
            {resume}
            
        Ensure that the title is descriptive and concise.
        You must return the title in the following format:
        
        json```
        {{
            "title": "title"
        }}
        ```
        
        Do not return any other information.
        """

        return self._llm.invoke(prompt)
