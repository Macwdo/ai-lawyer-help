import tempfile

from ai.services.document_manager import DocumentManager
from ai.services.pdf_manager import PDFManager
from common.models import File
from lawfirm.models.customer import CustomerIssue, CustomerIssueFile
from lawfirm.models.lawsuit import Lawsuit


class AiContextFeedService:
    def __init__(self):
        self._document_manager = DocumentManager()
        self._pdf_manager = PDFManager()

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
        customer_issue_file = CustomerIssueFile(
            customer_issue=customer_issue,
            file=file,
        )
        customer_issue_file.full_clean()
        customer_issue_file.save()

        documents = self.get_documents_from_file(file=file)

    def get_documents_from_file(self, *, file: File):
        documents = []

        match file.file_type:
            case File.Type.IMAGE_PNG | File.Type.IMAGE_JPEG:
                pass

            case File.Type.TEXT_PLAIN:
                pass

            case File.Type.APPLICATION_PDF:
                tmp_folder = tempfile.mkdtemp()
                with tempfile.NamedTemporaryFile(suffix=".pdf") as tmp_pdf_file:
                    tmp_pdf_file.write(file.file.read())
                    tmp_pdf_file.flush()
                    tmp_pdf_path = tmp_pdf_file.name

                    text = self._pdf_manager.extract_text(path=tmp_pdf_path)
                    images = self._pdf_manager.extract_images_from_pdf(
                        pdf_path=tmp_pdf_path,
                        output_folder=tmp_folder,
                    )

                documents = self._document_manager.from_text(text=text)

            case File.Type.AUDIO_MP3 | File.Type.AUDIO_WAV:
                pass

            case _:
                # TODO: Improve error handling
                raise ValueError(f"Unsupported file type: {file.Type}")

        return documents
