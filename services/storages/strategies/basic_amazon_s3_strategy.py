import sys

sys.path.append('../../../')

from models.amazon import amazon_s3_client
from amazon_s3_client import AmazonS3Client

class BasicAmazonS3Strategy:
    @classmethod
    def perform(cls, input_absolute_route, output_relative_route, content_type):
        AmazonS3Client
