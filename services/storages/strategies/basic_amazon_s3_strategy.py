from models.amazon.amazon_s3_client import AmazonS3Client
class BasicAmazonS3Strategy:
    @classmethod
    def perform(cls, input_absolute_route, output_relative_route, content_type):
        AmazonS3Client.upload_file(input_absolute_route,
            output_relative_route, content_type)
