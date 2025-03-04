from django.db.models.signals import pre_delete
from django.dispatch import receiver

from common.models import BaseModel, File
from common.tasks import delete_file_from_s3_task as delete_file_from_s3
from common.utils import get_file_related_fields

# @receiver(pre_delete, sender=File)
# def file_post_delete(sender, instance: File, **kwargs):
#     file = instance.file
#     delete_file_from_s3.delay(file_id=instance.pk)


@receiver(pre_delete, sender=BaseModel)
def base_model_post_delete(sender, instance, **kwargs):
    if isinstance(instance, File):
        delete_file_from_s3.delay(file_id=instance.pk)
        return

    file_fields = get_file_related_fields(instance)
    for field in file_fields:
        file = getattr(instance, field)
        delete_file_from_s3.delay(file_id=file.pk)
