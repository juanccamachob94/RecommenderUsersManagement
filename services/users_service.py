from services.user_creator_service import UserCreatorService
from services.user_saver_service import UserSaverService

class UsersService:
    @classmethod
    def create(cls, user, input_absolute_route, output_relative_route):
        UserCreatorService.perform(user, input_absolute_route, output_relative_route)
    
    @classmethod
    def save(cls, user, input_absolute_route, output_relative_route):
        # update or create record
        UserSaverService.perform(user, input_absolute_route, output_relative_route)

    @classmethod
    def update(cls, user):
        print("Actualizando el usuario" + user)


    @classmethod
    def delete(cls, user):
        print("Eliminando al usuario" + user)
