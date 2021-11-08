from models.amazon.amazon_s3_client import AmazonS3Client
from models.amazon.amazon_default_credentials_container import AmazonDefaultCredentialsContainer
class BasicAmazonS3Strategy:
    @classmethod
    def perform(cls, input_absolute_route, output_relative_route, content_type):
        amazon_credentials_container = AmazonDefaultCredentialsContainer()
        AmazonS3Client.upload_file(amazon_credentials_container, input_absolute_route,
            output_relative_route, content_type)
