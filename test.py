class Clase:
    @classmethod
    def foo(cls):
        print('ejecutando...')
        print(cls.__pfoo())
    
    @classmethod
    def __pfoo(cls):
        return "pfoo!!"

Clase.foo()
