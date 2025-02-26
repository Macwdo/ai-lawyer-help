# from os import getenv
# from .enviroment import DEBUG

CELERY_TIMEZONE = "America/Sao_Paulo"
CELERY_TASK_TRACK_STARTED = True

CELERY_BROKER_URL = "amqp://guest:guest@localhost:5672//"


# def get_aws_keys():
#     if not DEBUG:
#         aws_access_key = getenv("AWS_ACCESS_KEY_ID")
#         aws_secret_access_key = getenv("AWS_SECRET_ACCESS_KEY")
#
#     else:
#         aws_access_key = "dummy-id"
#         aws_secret_access_key = "dummy-secret"
#
#     return aws_access_key, aws_secret_access_key
#
#
# def get_aws_region():
#     if not DEBUG:
#         aws_region = getenv("AWS_REGION")
#     else:
#         aws_region = "us-east-1"
#
#     return aws_region
#
#
# def get_aws_endpoint_url():
#     if DEBUG:
#         return "http://localhost:4566"
#     else:
#         return getenv("AWS_ENDPOINT_URL")
# CELERY_BROKER_TRANSPORT_OPTIONS = {
#     "visibility_timeout": 3600,
#     "region": get_aws_region(),
#     "endpoint_url": get_aws_endpoint_url(),
#     "queue_name_prefix": "celery-",
# }

CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
