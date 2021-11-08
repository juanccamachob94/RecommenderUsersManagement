import boto
from boto.s3.key import Key
from helpers.url_helper import UrlHelper
from helpers.file_helper import FileHelper

class AmazonS3Client:
    instance = None

    @classmethod
    def upload_file(cls, amazon_credentials_container, output_relative_route, \
        input_absolute_route, content_type):
        uploaded = cls.get_instance(amazon_credentials_container) \
            .__upload(output_relative_route, input_absolute_route, content_type)
        if not uploaded:
            raise Exception(f'{output_relative_route} not uploaded correctly')


    @classmethod
    def get_instance(cls, amazon_credentials_container):
        if cls.instance == None:
            cls.instance = cls(amazon_credentials_container)
        return cls.instance


    def __init__(self, amazon_credentials_container):
        # the order of these attributes are very important
        self.amazon_credentials_container = amazon_credentials_container
        self.connection = self.__connect()
        self.bucket = self.__get_bucket()


    def __upload(self, output_relative_route, input_absolute_route, content_type=None, \
        callback=None, md5=None, reduced_redundancy=False):
        """
            based on https://stackabuse.com/example-upload-a-file-to-aws-s3-with-boto/
        """
        file = open(input_absolute_route, 'r+')
        file_to_upload_size = FileHelper.file_size(file)
        key = Key(self.bucket)
        key.key = self.amazon_credentials_container.get_relative_path() + output_relative_route
        if content_type:
            key.set_metadata('Content-Type', content_type)
        uploaded_file_size = key.set_contents_from_file(file, cb=callback, md5=md5, rewind=True,
            reduced_redundancy=reduced_redundancy)
        return uploaded_file_size == file_to_upload_size


    def __connect(self):
        return boto.connect_s3(self.amazon_credentials_container.get_access_key_id(), \
            self.amazon_credentials_container.get_secret_key())


    def __get_bucket(self):
        return self.connection.get_bucket(self.amazon_credentials_container.get_bucket_name(),
            validate=True)
