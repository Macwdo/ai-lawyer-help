from django.db import models

from common.models import BaseModel, File


class Lawfirm(BaseModel):
    name = models.CharField(max_length=200)
    logo = models.ForeignKey(
        File,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
