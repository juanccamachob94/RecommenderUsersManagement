import csv
import tempfile


from csv import DictWriter
from helpers.csv_helper import CSVHelper

from helpers.csv_helper import CSVHelper

class CSVManagementService:
    @classmethod
    def create_temporary_file(cls, model):
        temporary_file = tempfile.NamedTemporaryFile(suffix='.csv')
        with open(temporary_file.name, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(CSVHelper.build_headers_list(model))
        return temporary_file

    @classmethod
    def append_row(cls, csv_absolute_route, model):
        with open(csv_absolute_route, 'a', newline='') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=CSVHelper.build_headers_list(model))
            dictwriter_object.writerow(model.to_dict())
            f_object.close()
