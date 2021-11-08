from services.csv_management_service import CSVManagementService
from services.uploaders.temporary_uploader_service import TemporaryUploaderService
from helpers.url_helper import UrlHelper
from urllib.error import HTTPError

class DataManagementService:
    @classmethod
    def read(cls, input_file_route, model):
        try:
            return TemporaryUploaderService.perform(input_file_route)
        except (FileNotFoundError, HTTPError):
            if UrlHelper.extension(input_file_route) == 'csv':
                return CSVManagementService.create_temporary_file(model)
        return None
    
    @classmethod
    def append(cls, file, model):
        if UrlHelper.extension(file.name) == 'csv':
            return CSVManagementService.append_row(file, model, { 0: model.get_id() })
        return False
