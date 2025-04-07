from ai.services.ai.llm import LLMService
from ai.services.document_manager import DocumentManager

from ai.services.image_manager import ImageManager
from ai.services.pdf_manager import PDFFeedManager, PDFManager
from common.models import File
from common.services.files.file_utils import FileUtils
from lawfirm.models.customer import CustomerIssue
from lawfirm.models.lawsuit import Lawsuit


class AiContextFeedService:
    def __init__(self):
        self._document_manager = DocumentManager()
        self._pdf_manager = PDFManager()
        self._image_manager = ImageManager()
        self._llm_service = LLMService()

        self._file_utils = FileUtils()

        self._llm = self.__get_llm()
        self._ocr = self.__get_ocr_llm()

    def __get_llm(self):
        return self._llm_service.get_llm()

    def __get_ocr_llm(self):
        return self._llm_service.get_ocr_llm()

    def feed_ai_context(
        self,
        *,
        source_instance: CustomerIssue | Lawsuit,
        file: File,
    ):
        if isinstance(source_instance, Lawsuit):
            pass

        elif isinstance(source_instance, CustomerIssue):
            self._feed_ai_context_customer_issue(
                customer_issue=source_instance,
                file=file,
            )

        pass

    def _feed_ai_context_lawsuit(self, lawsuit: Lawsuit, file: File):
        pass

    def _feed_ai_context_customer_issue(
        self,
        *,
        customer_issue: CustomerIssue,
        file: File,
    ):
        documents = self.get_documents_from_file(file=file)

    def get_documents_from_file(self, *, file: File):
        documents = []

        match file.file_type:
            case File.Type.IMAGE_PNG | File.Type.IMAGE_JPEG:
                pass

            case File.Type.TEXT_PLAIN:
                pass

            case File.Type.APPLICATION_PDF:
                pdf_feed_manager = PDFFeedManager()
                pdf_feed_manager.extract(file=file)

            case File.Type.AUDIO_MP3 | File.Type.AUDIO_WAV:
                pass

            case _:
                # TODO: Improve error handling
                raise ValueError(f"Unsupported file type: {file.Type}")

        return documents
