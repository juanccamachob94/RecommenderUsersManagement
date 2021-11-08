from services.storages.strategies.basic_amazon_s3_strategy import BasicAmazonS3Strategy
class StorageService:
    @classmethod
    def perform(cls, input, output_route, content_type):
        BasicAmazonS3Strategy.perform(input, output_route, content_type)
