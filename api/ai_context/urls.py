from django.urls import path

from api.ai_context.views import AiContextFeedAPIView

app_name = "ai_context"

urlpatterns = [
    path("feed/", AiContextFeedAPIView.as_view(), name="feed"),
]
