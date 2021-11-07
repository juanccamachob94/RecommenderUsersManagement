import sys
sys.path.append('../')

from services.users_service import UsersService
class Client:
    @classmethod
    def main(cls):
        UsersService.create("user")
