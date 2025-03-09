from django.db import models


def upload_to(instance, filename: str):
    return f"files/{instance.file_name}"


def generate_code():
    import uuid

    return uuid.uuid4().hex[:12].upper()


class BaseModel(models.Model):
    code = models.CharField(
        max_length=12,
        default=generate_code,
        unique=True,
        db_index=True,
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.pk}-{self.code}-{self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"


class File(BaseModel):
    class Type(models.TextChoices):
        IMAGE_PNG = "image/png", "PNG Image"
        IMAGE_JPEG = "image/jpeg", "JPEG Image"
        TEXT_PLAIN = "text/plain", "Plain Text"
        APPLICATION_PDF = "application/pdf", "PDF File"
        AUDIO_MP3 = "audio/mpeg", "MP3 Audio"
        AUDIO_WAV = "audio/wav", "WAV Audio"

        # TODO: Support these file types
        # ("video/mp4", "Video (MP4)"),
        # ("image/gif", "Image (GIF)"),

    file = models.FileField(upload_to=upload_to, blank=True, null=True)

    original_file_name = models.TextField()

    file_name = models.CharField(max_length=255, unique=True)
    file_type = models.CharField(max_length=255, choices=Type.choices)

    upload_finished_at = models.DateTimeField(blank=True, null=True)

    @property
    def is_valid(self):
        """
        We consider a file "valid" if the the datetime flag has value.
        """
        return bool(self.upload_finished_at)
