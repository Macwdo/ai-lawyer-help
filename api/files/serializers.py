from rest_framework import serializers

from common.models import File


class FileDirectUploadStartApi(serializers.Serializer):
    file_name = serializers.CharField()
    file_type = serializers.ChoiceField(choices=File.Type.choices)


class FileDirectUploadFinishApi(serializers.Serializer):
    file_code = serializers.CharField()

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            "code",
            "created_at",
            "updated_at",
            "file",
            "original_file_name",
            "file_name",
            "file_type",
            "upload_finished_at",
        ]
