from celery import shared_task
from lawfirm.models import CustomerIssueFile


@shared_task
def sync_customer_issues_files_to_rag(customer_issue_file_id: int):
    """
    Sync customer issues files to RAG
    """

    pass


@shared_task
def sync_lawsuit_files_to_rag(lawsuit_file_id: int):
    """
    Sync lawsuit files to RAG
    """

    pass
