INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PART_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "django_celery_beat",
    "storages",
    "django_cleanup.apps.CleanupConfig",
    "corsheaders",
    "silk",
]

APPLICATION_APPS = [
    "common",
    "lawfirm",
]

INSTALLED_APPS += APPLICATION_APPS
INSTALLED_APPS += THIRD_PART_APPS
