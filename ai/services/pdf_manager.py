import io
import os

import fitz
import pytesseract
from pdf2image import convert_from_path
from PIL import Image


class PDFManager:
    def __init__(self):
        pass

    def extract_text(self, *, path: str):
        images = convert_from_path(path)
        extracted_text = ""

        for img in images:
            extracted_text += pytesseract.image_to_string(img) + "\n"

        return extracted_text

    def extract_images_from_pdf(self, *, pdf_path: str, output_folder: str):
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
