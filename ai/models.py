from django.db import models
from pgvector.django import VectorField

from common.models import BaseModel


# embedding is defined by ai Model
class OpenAIDocument3Small(BaseModel):
    text = models.TextField()
    embedding = VectorField(dimensions=1536)

    def __str__(self):
        return self.text[:50]


class OpenAIDocument3Large(BaseModel):
    text = models.TextField()
    embedding = VectorField(dimensions=3072)

    def __str__(self):
        return self.text[:50]
