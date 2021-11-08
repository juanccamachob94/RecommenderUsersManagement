import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from models.amazon.amazon_default_credentials_container import AmazonDefaultCredentialsContainer
from models.amazon.amazon_s3_client import AmazonS3Client
class Clase:
    XYZ = 123
    @classmethod
    def foo(cls):
        print('ejecutando...')
        x = cls()
        x.__ipfoo('dsda!!')
        print('finalizando')
    
    @classmethod
    def __pfoo(cls):
        return "pfoo!!"
    
    def __ipfoo(self, x):
        print('ejecutando ipfoo private instance method ' + x)


class Clase2(Clase):
    XYZ = 456
    def launch(self):
        print(self.__class__.XYZ)


# Clase.foo()
# Clase2().launch()
AmazonS3Client.upload_file(AmazonDefaultCredentialsContainer(), 'jisoo1.jpg',
                           'jisoo.jpg', 'text/csv')
