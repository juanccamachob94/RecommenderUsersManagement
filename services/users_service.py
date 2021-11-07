class UsersService:
    @classmethod
    def create(cls, user):
        print("Creando el usuario" +  user)


    @classmethod
    def update(cls, user):
        print("Actualizando el usuario" + user)


    @classmethod
    def delete(cls, user):
        print("Eliminando al usuario" + user)
