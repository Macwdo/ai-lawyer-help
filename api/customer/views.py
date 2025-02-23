from api.customer.serializers import CustomerSerializer
from common.views import BaseModelViewSet
from lawfirm.models import Customer


class CustomerModelViewSet(BaseModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
