import uuid, boto3
from botocore.client import Config
from django.conf import settings

# Helper class to aid aws s3 operations
class S3Helper:
    s3_client = boto3.client('s3',
                             config=Config(signature_version='s3v4'),
                             aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                             region_name=settings.S3_BUCKET_REGION)

    def create_presigned_url(self, bucket_name, object_name, key_prefix):
        """
        Generate a presigned URL to share an S3 object
        """
        return self.s3_client.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': bucket_name,
                'Key': "{}/{}/{}".format(key_prefix, uuid.uuid4().hex, object_name),
                'ACL': 'public-read-write',
            },
            ExpiresIn=604799,
        )

    def download(self, bucket, key, new_file_name):
        self.s3_client.download_file(bucket, key, new_file_name)
        return new_file_name

    def upload_public_file(self, file_path, bucket_name, object_name, key_prefix):
        key = "{}/{}/{}".format(key_prefix, uuid.uuid4().hex, object_name)
        self.s3_client.upload_file(file_path, bucket_name, key, ExtraArgs={'ACL': 'public-read'})
        _s3_link = f"https://{bucket_name}.s3.{settings.S3_BUCKET_REGION}.amazonaws.com/{key}"
        return _s3_link


s3_helper = S3Helper()
