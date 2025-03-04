from django.shortcuts import get_object_or_404
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from api.files.serializers import (
    FileDirectUploadFinishApi,
    FileDirectUploadStartApi,
    FileSerializer,
)
from common.models import File
from common.services.files.file_direct_upload import FileDirectUploadService
from common.views import BaseGenericViewSet


class FileViewSet(BaseGenericViewSet, mixins.DestroyModelMixin):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    @action(detail=False, methods=["post"], url_path="upload-start")
    def direct_upload_start(self, request: Request):
        serializer = FileDirectUploadStartApi(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = FileDirectUploadService()
        presigned_data = service.start(**serializer.validated_data)  # type: ignore

        return Response(presigned_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], url_path="upload-finish")
    def direct_upload_finish(self, request: Request):
        serializer = FileDirectUploadFinishApi(data=request.data)
        serializer.is_valid(raise_exception=True)

        file_code = serializer.validated_data["file_code"]  # type: ignore
        file = get_object_or_404(File, code=file_code)

        service = FileDirectUploadService()
        service.finish(file=file)

        return Response("File uploaded successfully", status=status.HTTP_200_OK)
