import csv
import tempfile

from csv import DictWriter
from helpers.csv_helper import CSVHelper
from helpers.application_helper import ApplicationHelper

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
        if cls.__registered_row(file, dict_positions_values):
            return False
        cls.__append(file.name, model)
        return True

    
    @classmethod
    def append_or_update_row(cls, file, model, dict_positions_values):
        registered_row = cls.__registered_row(file, dict_positions_values)
        if registered_row:
            cls.__replace(file.name, model, registered_row)
        else:
            cls.__append(file.name, model)
        return True


    @classmethod
    def __append(cls, file_route, model, model_dict=None):
        with open(file_route, 'a', newline='') as f_object:  # this file.name represents the route
            dictwriter_object = DictWriter(f_object, fieldnames=CSVHelper.build_headers_list(model))
            dictwriter_object.writerow(model_dict if model_dict else model.to_dict())
            f_object.close()
    
    @classmethod
    def __replace(cls, file_route, model, registered_row):
        new_dict = cls.__build_merged_dict(model, registered_row)
        cls.__remove(cls, file_route, model)
        cls.__append(file_route, model)
    
    @classmethod
    def __remove(cls, file_route, model):
        pass


    @classmethod
    def __registered_row(cls, file, dict_positions_values):
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
                    return row
            except StopIteration:
                break
        return None


    @classmethod
    def __rows_lazy_iterator(cls, file_route):
        # it has logic to use generator and produce results with lazy iteration
        with open(file_route, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                yield row


    @classmethod
    def __build_merged_dict(cls, model, current_register_row):
        current_register_dict = ApplicationHelper \
            .keys_values_to_dict(CSVHelper.build_headers_list(model), current_register_row)
        new_register_dict = model.to_dict()
        for key in current_register_dict:
            if new_register_dict[key]:
                current_register_dict[key] = new_register_dict[key]
        return current_register_dict

    @classmethod
    def __rows_filtered_lazy_iterator(cls, file, dict_positions_values):
        pass
