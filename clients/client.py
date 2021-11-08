import sys

sys.path.append('../')

from models.user import User
from services.users_service import UsersService

class Client:
    @classmethod
    def main(cls):
        user = User(1, 'User 1 to test')
        UsersService.create(user)
