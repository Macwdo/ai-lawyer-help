from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from api.customer.issues.views import (
    CustomerIssueModelViewSet,
)
from api.customer.views import CustomerModelViewSet
from api.files.views import FileViewSet

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
    lookup="issue",
)

files_router = routers.SimpleRouter()
files_router.register(r"files", FileViewSet, basename="files")


urlpatterns = []
urlpatterns += (
    router.urls + customer_router.urls + issue_router.urls + files_router.urls
)
