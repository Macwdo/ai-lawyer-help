import io
import os

import fitz
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

from langchain_core.documents import Document
from ai.services.ai.llm import LLMService
from ai.services.document_manager import DocumentManager
from ai.services.image_manager import ImageManager
from common.models import File
from common.services.files.file_utils import FileUtils


class PDFManager:
    def __init__(self):
        pass

    def extract_text(self, path: str):
        images = convert_from_path(path)
        extracted_text = ""

        for img in images:
            extracted_text += pytesseract.image_to_string(img) + "\n"

        return extracted_text

    def extract_images_from_pdf(self, pdf_path: str, output_folder: str):
        """Extracts and saves images from a PDF."""

        os.makedirs(output_folder, exist_ok=True)
        doc = fitz.open(pdf_path)

        for page_number, page in enumerate(doc):  # type: ignore
            for img_index, img in enumerate(page.get_images(full=True)):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                img_format = base_image["ext"]  # Get image format (e.g., "png", "jpeg")

                # Save image
                image = Image.open(io.BytesIO(image_bytes))
                image_filename = os.path.join(
                    output_folder,
                    f"page_{page_number + 1}_img_{img_index + 1}.{img_format}",
                )
                image.save(image_filename)
                print(f"Saved Image: {image_filename}")

        return output_folder


# 1 - Extract text from PDF
# 2 - Extract images from PDF
# 3.1 - Resume Image
# 3.2 - Categorize Generic Image
# 3.3 - Generate Image Title
# 4 - Resume Pdf
# 5 - Categorize Image Based On Pdf Resume
# 6 - Generate Document
# 7 - Attach Metadata to Document


class PDFFeedManager:
    def __init__(self):
        self._document_manager = DocumentManager()
        self._pdf_manager = PDFManager()
        self._image_manager = ImageManager()
        self._llm_service = LLMService()

        self._file_utils = FileUtils()

        self._llm = self._llm_service.get_llm()
        self._rllm = self._llm_service.get_reasoning_llm()

    def extract(self, file: File):
        file_bytes = file.file.read()
        # 1 - Extract text from PDF
        with self._file_utils.write_tmp_pdf(file_bytes) as pdf_path:
            text = self._pdf_manager.extract_text(pdf_path)
            documents = self._document_manager.from_text(text)
            new_documents = []

            for document in documents:
                text = self._adjust_extracted_text(document)
                document.page_content = text
                new_documents.append(document)

        #         # 2 - Extract images from PDF
        # with self._file_utils.temp_folder() as tmp_folder:
        #             self._pdf_manager.extract_images_from_pdf(pdf_path, tmp_folder)

        #             images_path = os.listdir(tmp_folder)
        #             images_full_path = [
        #                 os.path.join(tmp_folder, image) for image in images_path
        #             ]

        #             # 3 - Resume Images
        #             images_map = self._map_images(images_full_path)

    def _adjust_extracted_text(self, document: Document, input_language: str = "pt-br"):
        prompt = """
        The following text has been extracted from a PDF document. It may contain language errors, formatting issues, and unwanted characters due to the extraction process.

        The language of the text is __input_language__.

        Your task is to:
        1. Correct any language errors (grammar, spelling, punctuation, etc.).
        2. Fix formatting issues to improve readability.
        3. Remove any unwanted characters or artifacts introduced during extraction.

        Ensure the output is clean, well-structured, and retains the original meaning of the text.
        Here is the document text:
        
        __extracted_text__
        
        Your work is fix grammar, spelling, punctuation, formatting issues.
        Do not generate new content or change the original meaning of the text.
        """

        prompt = prompt.replace("__input_language__", input_language)
        prompt = prompt.replace("__extracted_text__", document.page_content)

        return self._rllm.invoke(prompt)

    def _map_images(self, images_path: list[str]):
        images = []
        for image in images_path:
            image_resume = self._image_manager.resume_image(image)
            image_title = self._image_manager.generate_image_title_from_resume(
                image_resume
            )

            image_data = {"path": image, "resume": image_resume, "title": image_title}
            images.append(image_data)

        return images
