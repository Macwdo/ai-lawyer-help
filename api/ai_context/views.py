from rest_framework import status
from rest_framework.response import Response

from common.views import BaseAPIView


class AiContextFeedAPIView(BaseAPIView):
    def get(self, request):
        return Response("File uploaded successfully", status=status.HTTP_200_OK)
