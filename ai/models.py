from django.db import models
from pgvector.django import VectorField


class OpenAIDocument3Small(models.Model):
    text = models.TextField()
    embedding = VectorField(dimensions=1536)

    def __str__(self):
        return self.text[:50]


class OpenAIDocument3Large(models.Model):
    text = models.TextField()
    embedding = VectorField(dimensions=3072)

    def __str__(self):
        return self.text[:50]
