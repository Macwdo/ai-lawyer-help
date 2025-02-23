from django.db import models


def generate_code():
    import uuid
    return uuid.uuid4().hex[:8].upper()

class BaseModel(models.Model):
    code = models.CharField(
        max_length=8,
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
        return f"{self.__class__.__name__} - {self.pk}"

class File(BaseModel):
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    # Add Behavior to delete file by cascade
    presigned_url = models.URLField(blank=True, null=True)
    presigned_upload_complete = models.BooleanField(default=None, null=True)

