from rest_framework import serializers

from common.models import File


class FileDirectUploadStartApi(serializers.Serializer):
    file_name = serializers.CharField()
    file_type = serializers.CharField()


class FileDirectUploadFinishApi(serializers.Serializer):
    file_code = serializers.CharField()


# "id": 14,
# "code": "CDEF32F23CDA",
# "created_at": "2025-03-03T20:54:16.086795-03:00",
# "updated_at": "2025-03-03T20:54:16.210923-03:00",
# "file": "http://localhost:8000/media/files/1d9311b877ae4349a867501f46ad8025.txt",
# "original_file_name": "text.txt",
# "file_name": "1d9311b877ae4349a867501f46ad8025.txt",
# "file_type": "text/plain",
# "upload_finished_at": "2025-03-03T20:54:16.207834-03:00"


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
