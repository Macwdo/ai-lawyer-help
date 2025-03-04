import pathlib
from uuid import uuid4

from django.db import transaction
from django.utils import timezone

from common.models import File, upload_to
from common.services.files.aws_s3_storage import S3StorageService
from common.services.loggers.app_logger import ApplicationLogger


def file_generate_name(original_file_name):
    extension = pathlib.Path(original_file_name).suffix

    return f"{uuid4().hex}{extension}"


class FileDirectUploadService:
    def __init__(self):
        self._s3_storage_service = S3StorageService()

    @transaction.atomic
    def start(self, *, file_name: str, file_type: str):
        file = File(
            original_file_name=file_name,
            file_name=file_generate_name(file_name),
            file_type=file_type,
            file=None,
        )
        file.full_clean()
        file.save()

        upload_path = upload_to(file, file.file_name)

        file.file = file.file.field.attr_class(file, file.file.field, upload_path)
        file.save()

        presigned_data = self._s3_storage_service.generate_presigned_url(
            file_path=upload_path,
            file_type=file.file_type,
        )

        return {"code": file.code, **presigned_data}

    @transaction.atomic
    def finish(self, *, file: File) -> File:
        file.upload_finished_at = timezone.now()
        file.full_clean()
        file.save()

        return file


class FileService:
    def __init__(self):
        self._file_direct_upload_service = FileDirectUploadService()
        self._s3_storage_service = S3StorageService()
        self._application_logger = ApplicationLogger()

    @transaction.atomic
    def delete(self, *, file: File):
        file.delete()
        self.delete_from_s3(file=file)

    def delete_from_s3(self, *, file: File):
        file_path = upload_to(file, filename=file.file_name)
        self._application_logger.info(
            f"Deleting file from S3: {file_path}. File ID: {file.pk}"
        )
        self._s3_storage_service.delete_file(file_path=file_path)
