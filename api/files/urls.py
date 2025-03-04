from rest_framework import routers

from api.files.views import FileViewSet

app_name = "files"

files_router = routers.SimpleRouter()
files_router.register(r"", FileViewSet, basename="files")

urlpatterns = []
urlpatterns += files_router.urls
