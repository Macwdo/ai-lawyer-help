import boto3
from django.conf import settings


class S3StorageService:
    def get_s3_client(self):
        return boto3.client(
            service_name="s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME,
        )

    def generate_presigned_url(self, *, file_path: str, file_type: str):
        s3_client = self.get_s3_client()

        acl = settings.AWS_DEFAULT_ACL
        expires_in = settings.AWS_PRESIGNED_EXPIRE

        presigned_data = s3_client.generate_presigned_post(
            settings.AWS_STORAGE_BUCKET_NAME,
            file_path,
            Fields={"acl": acl, "Content-Type": file_type},
            Conditions=[
                {"acl": acl},
                {"Content-Type": file_type},
            ],
            ExpiresIn=expires_in,
        )

        return presigned_data

    def delete_file(self, *, file_path: str):
        s3_client = self.get_s3_client()
        s3_client.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=file_path)
