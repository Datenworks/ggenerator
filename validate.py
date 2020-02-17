import json
from sys import argv


class Dataset(object):

    def __init__(self, filepath):
        self.file = filepath

    def get_parameters(self):
        files = [open(self.file, 'r').read()]   
        for spec in files:
           self.parameters = json.loads(spec)
        for id in self.parameters.get('datasets').keys():
            dataset = self.parameters.get('datasets').get(id)
        return dataset

class Dataset_Size_Validator(object):

    def __init__ (self, dataset):
        self.dataset = dataset

    def verify_size(self):
        if 'size' in self.dataset:
            if isinstance(self.dataset.get('size'), int) and self.dataset.get('size') > 0:
                self.size = self.dataset.get('size')
            else:
                raise "Size must be integer and higher than 0"
        else:
            raise "Dont Found Size"

class Dataset_Format_Validator(object):

    def __init__ (self, dataset):
        self.dataset = dataset

    def verify_format(self):
        if 'format' in self.dataset:
            if 'header' in self.dataset.get('format'):
                if isinstance(self.dataset.get('format').get('header'), bool):
                    self.format_header = self.dataset.get('format').get('header')
                else:
                    raise "Format Header must be boolean"
            else:
                raise "Dont Found Header"

            if 'type' in self.dataset.get('format'):
                if isinstance(self.dataset.get('format').get('type'),str):
                    self.format_type = dataset.get('format').get('type')
                else:
                    raise "Format Type must be csv or json"
            else:
                raise "Dont Found Type"
        else:
            raise "Dont Found Format"

class Dataset_Fields_Validator(object):

    def __init__(self, dataset):
        self.dataset = dataset

    def verify_fields(self):
        if 'fields' in self.dataset:
            self.field = dataset.get('fields')
            body =  self.field
            for body_field in body:
                if 'name' in body_field:
                    if isinstance(body_field.get('name'), str):
                        self.field_name = body_field.get('name')
                    else:
                        raise "Name type must be string"
                else:
                    raise "Dont Found Name in Fields"
                if 'generator' in body_field:
                    if isinstance(body_field.get('generator'), dict):
                        self.field_generator = body_field.get('generator')
                    else:
                        raise "Generator must be dict"
                else:
                    raise "Dont Found Generator in Fields"
                if 'type' in body_field:
                    if isinstance(body_field.get('type'), (str, bool, float, int, list)):
                        self.field_generator = body_field.get('type')
                    else:
                        raise "Type is not "
                else:
                    raise "Dont Found Type in Fields"
        else:
            raise "Dont Found Fields"

class Dataset_Serializer_Validator(object):

    def __init__(self, dataset):
        self.dataset = dataset

    def verify_serializers(self):
        if 'serializers' in self.dataset:
            if 'to' in self.dataset.get('serializers'):
                self.serializer_to = dataset.get('serializers').get('to')
                body_to = self.serializer_to 
                for dict_to in body_to:
                    if 'type' in dict_to:
                        if isinstance(dict_to.get('type'), str):
                            self.serializer_type = dict_to.get('type')
                        else:
                            raise "Serializer type must be string"
                    else:
                        raise "Dont Found Type in Serializers"
                    if 'uri' in dict_to:
                        if isinstance(dict_to.get('uri'),str):
                            self.serializer_uri = dict_to.get('uri')
                        else: 
                            raise "uri error"
                    else:
                        raise "Dont Found uri in Serializers"
            else:
                raise "Dont Found TO in Serializers"
        else:
            raise "Dont Found Serializers"


if __name__ == "__main__":
    
    spec = Dataset("fake_generator_sample.txt")
    dataset = spec.get_parameters()
    size_validator = Dataset_Size_Validator(dataset) 
    format_validator = Dataset_Format_Validator(dataset)
    field_validator = Dataset_Fields_Validator(dataset)
    serializer_validator = Dataset_Serializer_Validator(dataset) 

    script_name = argv[0]
    action = argv[1]

    if action == 'size_validator':
        size_validator.verify_size()
    elif action == 'format_validator':
        format_validator.verify_format()
    elif action == 'field_validator':
        field_validator.verify_fields()
    elif action == 'serializer_validator':
        serializer_validator.verify_serializers() 
    else:
        print("Command not found")