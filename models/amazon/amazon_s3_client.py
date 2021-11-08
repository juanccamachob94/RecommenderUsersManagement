import boto3
class AmazonS3Client:
    instance = None

    @classmethod
    def upload_file(cls, amazon_credentials_container, output_relative_route, \
        input_absolute_route, content_type):
        cls.get_instance(amazon_credentials_container) \
            .__upload(output_relative_route, input_absolute_route, content_type)
    

    @classmethod
    def get_instance(cls, amazon_credentials_container):
        if cls.instance == None:
            cls.instance = cls(amazon_credentials_container)
        return cls.instance


    def __init__(self, amazon_credentials_container):
        self.amazon_credentials_container = amazon_credentials_container
        self.connection = self.__connect()


    def __upload(self, output_relative_route, input_absolute_route, content_type):
        print('subiendo archivo CSV?...')
    

    def __connect(self):
        return boto3.resource('s3', self.amazon_credentials_container.get_access_key_id(), \
            self.amazon_credentials_container.get_secret_key())
