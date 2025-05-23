# Generated by Django 5.1.6 on 2025-03-04 08:00

import pgvector.django.vector
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("ai", "0001_vector"),
    ]

    operations = [
        migrations.CreateModel(
            name="OpenAIDocument3Large",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("embedding", pgvector.django.vector.VectorField(dimensions=3072)),
            ],
        ),
        migrations.CreateModel(
            name="OpenAIDocument3Small",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("embedding", pgvector.django.vector.VectorField(dimensions=1536)),
            ],
        ),
    ]
