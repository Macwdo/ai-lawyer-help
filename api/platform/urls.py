from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from api.platform.customer.issues.views import CustomerIssueModelViewSet
from api.platform.customer.views import CustomerModelViewSet

app_name = "platform"

router = routers.SimpleRouter()

router.register(r"customers", CustomerModelViewSet, basename="customers")
customer_router = nested_routers.NestedSimpleRouter(
    router,
    r"customers",
    lookup="customer",
)
customer_router.register(
    r"issues",
    CustomerIssueModelViewSet,
    basename="customer-issues",
)

issue_router = nested_routers.NestedSimpleRouter(
    customer_router,
    r"issues",
    lookup="issue",
)

urlpatterns = []
urlpatterns += router.urls + customer_router.urls + issue_router.urls
