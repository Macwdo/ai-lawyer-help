from rest_framework import serializers

from api.serializers import CodeRelatedField
from common.models import File


class AiContextUploadSerializer(serializers.Serializer):
    file_code = CodeRelatedField(model=File)
