import sys
sys.path.append('../')

from services.user_creator_service import UserCreatorService

class UsersService:
    @classmethod
    def create(cls, user):
        UserCreatorService.perform(user)

    @classmethod
    def update(cls, user):
        print("Actualizando el usuario" + user)


    @classmethod
    def delete(cls, user):
        print("Eliminando al usuario" + user)
