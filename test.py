import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
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



class Clase3:
    instance = None

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()
        return cls.instance

class Clase4(Clase3):
    pass

import csv

my_generator = csv_rows()

while True:
    try:
        row = next(my_generator)
    except StopIteration:
        break

# Clase.foo()
# Clase2().launch()
#AmazonS3Client.upload_file(AmazonDefaultCredentialsContainer(), 'jisoo1.jpg',
#                          'jisoo.jpg', 'text/csv')



def metodo(**algo):
    print(algo)
