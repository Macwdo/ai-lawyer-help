from . import AWS_STORAGE_BUCKET_NAME, BASE_DIR

# Static files
STATIC_PATH = "static"
STATIC_URL = f"/{STATIC_PATH}/"
STATIC_ROOT = BASE_DIR / f"{STATIC_PATH}"
STATICFILES_DIRS = [BASE_DIR / "staticfiles"]

# Media files
MEDIA_PATH = "media"
MEDIA_URL = f"/{MEDIA_PATH}/"
MEDIA_ROOT = BASE_DIR / f"{MEDIA_PATH}"

# MEDIA_STORAGE = "django.core.files.storage.FileSystemStorage"
# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# Storages
S3_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STORAGES = {
    "default": {
        "BACKEND": S3_FILE_STORAGE,
        "OPTIONS": {
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
            # WARN: Facing problem with presigned url upload when media path is set
            "location": "",
        },
    },
    "staticfiles": {
        "BACKEND": S3_FILE_STORAGE,
        "OPTIONS": {
            "location": STATIC_PATH,
        },
    },
}
