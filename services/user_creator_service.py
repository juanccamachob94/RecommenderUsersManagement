from services.storages.storage_service import StorageService
from helpers.file_helper import FileHelper
from services.data_management_service import DataManagementService

class UserCreatorService:
    @classmethod
    def perform(cls, user, input_file_absolute_route, output_relative_route):
        temporary_file = DataManagementService.read(input_file_absolute_route, user)
        DataManagementService.append(temporary_file, user)
        StorageService.perform(temporary_file.name, output_relative_route,
            FileHelper.content_type(input_file_absolute_route))
