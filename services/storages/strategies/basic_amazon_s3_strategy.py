from models.amazon.amazon_s3_client import AmazonS3Client
from models.amazon.amazon_default_credentials_container import AmazonDefaultCredentialsContainer
from services.uploaders.temporary_uploader_service import TemporaryUploaderService
from factories.amazon_credentials_containers_factory import AmazonCredentialsContainerFactory
class BasicAmazonS3Strategy:
    @classmethod
    def perform(cls, input_absolute_route, output_relative_route, content_type):
        temporary_file = TemporaryUploaderService.perform(input_absolute_route)
        AmazonS3Client.upload_file(AmazonCredentialsContainerFactory.get_default_instance(), \
            temporary_file.name, output_relative_route, content_type)
