from django.db import models

from common.models import BaseModel


class Settings(BaseModel):
    class Meta:
        abstract = True

    name = models.CharField(max_length=200)
    enabled = models.BooleanField(default=True)


# TODO: Create a Settings to define models dynamically
class ApplicationSettings(Settings):
    name = models.CharField(max_length=200)
