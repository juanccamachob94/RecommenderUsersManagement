from services.user_creator_service import UserCreatorService

class UsersService:
    @classmethod
    def create(cls, user, input_absolute_route, output_relative_route):
        UserCreatorService.perform(
            user, input_absolute_route, output_relative_route)

    @classmethod
    def update(cls, user):
        print("Actualizando el usuario" + user)


    @classmethod
    def delete(cls, user):
        print("Eliminando al usuario" + user)
