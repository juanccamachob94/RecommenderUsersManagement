import csv
import tempfile

from csv import DictWriter
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
    def append_row(cls, file, model, dict_positions_values):
        if cls.__is_registered_row(file, dict_positions_values):
            return False
        with open(file.name, 'a', newline='') as f_object: # this file.name represents the route
            dictwriter_object = DictWriter(f_object, fieldnames=CSVHelper.build_headers_list(model))
            dictwriter_object.writerow(model.to_dict())
            f_object.close()
        return True


    @classmethod
    def __is_registered_row(cls, file, dict_positions_values):
        """
            The last parameter uses the positions ids on row array with the respective values
            to match the data and validate if the row is registered. The most basic use of this
            method would use the position that belongs to id of record ({ 0: 'id' })
        """
        # file.name is usted to represent the file location
        rows_generator = cls.__rows_lazy_iterator(file.name)
        matched = None
        while True:
            try:
                row = next(rows_generator)
                matched = True
                for position in dict_positions_values:
                    matched = matched and str(row[position]) == str(dict_positions_values[position])
                if matched:
                    return True
            except StopIteration:
                break
        return False


    @classmethod
    def __rows_lazy_iterator(cls, file_route):
        # it has logic to use generator and produce results with lazy iteration
        with open(file_route, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                yield row
