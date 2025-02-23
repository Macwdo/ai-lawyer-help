from rest_framework_nested import routers as nested_routers
from rest_framework import routers

from api.customer.issues.views import (
    CustomerIssueFileModelViewSet,
    CustomerIssueModelViewSet,
)
from api.customer.views import CustomerModelViewSet

router = routers.SimpleRouter()

# Registrar a rota principal para customers
router.register(r"customers", CustomerModelViewSet, basename="customers")

# Criar rota aninhada para customer-issues
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
    lookup="issue",  # This makes "<issue-code>" available
)
issue_router.register(
    r"files",
    CustomerIssueFileModelViewSet,
    basename="customer-issue-files",
)

urlpatterns = router.urls + customer_router.urls + issue_router.urls
