from services.storages.storage_service import StorageService
class UserCreatorService:
    @classmethod
    def perform(cls, user, data_manager):
        print('Se ha mandado al usuario' + str(type(user)))
        StorageService.perform('input', 'output', 'content_type')
        print('Se ha terminado de ejecutar')
        