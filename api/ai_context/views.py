from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from ai.services.ai_context_feed import AiContextFeedService
from api.ai_context.serializers import AiContextUploadSerializer
from common.models import File
from common.views import BaseAPIView
from lawfirm.models.customer import CustomerIssue
from lawfirm.models.lawsuit import Lawsuit


class AiContextFeedAPIView(BaseAPIView):
    def post(self, request):
        serializer = AiContextUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        source_instance = None
        if data["source"] == "customer_issue":  # type: ignore
            source_instance = get_object_or_404(
                CustomerIssue,
                code=data["source_code"],  # type: ignore
            )

        elif data["source"] == "lawsuit":  # type: ignore
            source_instance = get_object_or_404(
                Lawsuit,
                code=data["source_code"],  # type: ignore
            )

        else:
            return Response("Invalid source", status=status.HTTP_400_BAD_REQUEST)

        file = get_object_or_404(File, code=data["file_code"])  # type: ignore

        service = AiContextFeedService()
        service.feed_ai_context(source_instance=source_instance, file=file)

        return Response("File uploaded successfully", status=status.HTTP_200_OK)
