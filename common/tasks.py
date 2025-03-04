from celery import shared_task


@shared_task
def delete_file_from_s3_task(file_id: int):
    from common.models import File
    from common.services.files.file_direct_upload import FileService

    file = File.objects.get(pk=file_id)
    service = FileService()
    service.delete_from_s3(file=file)
