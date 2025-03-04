from django.urls import include, path

urlpatterns = [
    path("platform/", include("api.platform.urls")),
    path("files/", include("api.files.urls")),
    path("ai-context/", include("api.ai_context.urls")),
]
