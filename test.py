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

Clase.foo()

Clase2().launch()
