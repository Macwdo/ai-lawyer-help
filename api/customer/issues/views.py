from api.customer.issues.serializers import (
    CustomerIssueSerializer,
)
from common.views import BaseModelViewSet
from lawfirm.models.customer import Customer, CustomerIssue


class CustomerIssueModelViewSet(BaseModelViewSet):
    queryset = CustomerIssue.objects.all()
    serializer_class = CustomerIssueSerializer

    parent_model = Customer
    nested_field = "code"
    nested_prefix = "customer"
