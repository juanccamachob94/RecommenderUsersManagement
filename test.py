import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from services.uploaders.temporary_uploader_service import TemporaryUploaderService

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


print("X temporay a punto de ejecutar")
x = TemporaryUploaderService.perform(
    'https://somoskudasai.com/wp-content/uploads/2021/02/portada_hunter-x-hunter-6.jpg')

print('Se ha terminado de obtener el valor de x')

file_descriptor_identifier = x.fileno() # <int>
file_descriptor_status = os.fstat(file_descriptor_identifier) # <os.stat_result>
file_size = file_descriptor_status.st_size

sk = x.seek(0, os.SEEK_END)
print('sk: ', str(type(sk)), sk)
print('tell: ', x.tell())
print('f: ' + str(type(x)))


print('Este mensaje no va a salir')


# Clase.foo()
# Clase2().launch()
