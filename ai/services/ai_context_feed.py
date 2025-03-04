from ai.services.embeddings import EmbeddingManager
from common.models import File
from lawfirm.models.customer import CustomerIssue, CustomerIssueFile
from lawfirm.models.lawsuit import Lawsuit


class AiContextFeedService:
    class AiContextFileSources:
        LAWSUIT = "lawsuit"
        CUSTOMER_ISSUE = "customer_issue"

    def __init__(self):
        self._embeddings_service = EmbeddingManager()

    def feed_ai_context(self, *, source_instance: CustomerIssue | Lawsuit, file: File):
        if isinstance(source_instance, Lawsuit):
            pass

        elif isinstance(source_instance, CustomerIssue):
            pass

        pass

    def _feed_ai_context_lawsuit(self, lawsuit: Lawsuit, file: File):
        pass

    # TODO: Test it and download file from s3
    def _feed_ai_context_customer_issue(
        self, customer_issue: CustomerIssue, file: File
    ):
        customer_issue_file = CustomerIssueFile(
            customer_issue=customer_issue,
            file=file,
        )
        customer_issue_file.full_clean()
        customer_issue_file.save()
