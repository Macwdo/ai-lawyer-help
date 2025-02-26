from rest_framework import status
from rest_framework.response import Response
from api.customer.issues.serializers import (
    CustomerIssueFileSerializer,
    CustomerIssueSerializer,
)
from common.views import BaseModelViewSet
from customer_onboarding.tasks import sync_customer_issues_files_to_rag
from lawfirm.models import Customer, CustomerIssue, CustomerIssueFile


class CustomerIssueModelViewSet(BaseModelViewSet):
    queryset = CustomerIssue.objects.all()
    serializer_class = CustomerIssueSerializer

    parent_model = Customer
    nested_field = "code"
    nested_prefix = "customer"

    def get_queryset(self):
        return (
            super().get_queryset().filter(customer__code=self.kwargs["customer_code"])
        )


class CustomerIssueFileModelViewSet(BaseModelViewSet):
    queryset = CustomerIssueFile.objects.all()
    serializer_class = CustomerIssueFileSerializer

    parent_model = CustomerIssue
    nested_field = "code"
    nested_prefix = "issue"

    def get_queryset(self):
        queryset = (
            super()
            .get_queryset()
            .filter(
                issue__customer__code=self.kwargs["customer_code"],
                issue__code=self.kwargs["issue_code"],
            )
        )

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        customer_issue_file_id = serializer.instance.pk
        sync_customer_issues_files_to_rag.delay(customer_issue_file_id)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
