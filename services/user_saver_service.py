from services.data_management_service import DataManagementService

class UserSaverService:
    @classmethod
    def perform(user, input_absolute_route, output_relative_route):
        temporary_file = DataManagementService.read(input_absolute_route, user)
