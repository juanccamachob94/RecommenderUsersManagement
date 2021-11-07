class StorageService:
    @classmethod
    def perform(cls, input, output_route, content_type):
        BasicS3Strategy.perform(input, output_route, content_type)
