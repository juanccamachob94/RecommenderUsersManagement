import sys
import time



sys.path.append('../')

from models.user import User
from services.users_service import UsersService
from services.uploaders.temporary_uploader_service import TemporaryUploaderService

class Client:
    @classmethod
    def main(cls):
        user = User(1, 'User 1 to test')
        print(user)
        xyz = TemporaryUploaderService.perform(
            'https://somoskudasai.com/wp-content/uploads/2021/02/portada_hunter-x-hunter-6.jpg'
        )
        print('sleep....' + str(type(xyz)) + ' - ' + xyz.name)
        print('finish!')
        # UsersService.create(user)
