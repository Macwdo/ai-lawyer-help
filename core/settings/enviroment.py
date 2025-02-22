from os import getenv

SECRET_KEY = getenv("SECRET", "django-insecure")
DEBUG = getenv("DEBUG", "1") == "1"
ALLOWED_HOSTS = getenv("ALLOWED_HOSTS", "*,").split(",")

# Environment Variables
OPENAI_ORGANIZATION = getenv("OPENAI_ORGANIZATION", "organization")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "api_key")
