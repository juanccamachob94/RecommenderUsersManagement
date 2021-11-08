from models.user import User
from services.users_service import UsersService
from factories.amazon_credentials_containers_factory import AmazonCredentialsContainerFactory

class Client:
    @classmethod
    def main(cls):
        csv_filename = 'users.csv'
        user = User(2, 'User 2 to validate new record')
        input_path = AmazonCredentialsContainerFactory.get_default_instance().get_absolute_path()
        UsersService.create(user, f'{input_path}{csv_filename}', csv_filename)
