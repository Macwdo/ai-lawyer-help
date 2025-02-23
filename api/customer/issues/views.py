from api.customer.issues.serializers import (
    CustomerIssueFileSerializer,
    CustomerIssueSerializer,
)
from common.views import BaseModelViewSet
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
