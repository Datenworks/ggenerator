import json
from sys import argv


class Dataset(object):

    def __init__(self, filepath):
        self.file = filepath

    def get_parameters(self):
        files = open(self.file, 'r').read()
        self.parameters = json.loads(files)
        for id in self.parameters.get('datasets').keys():
            dataset = self.parameters.get('datasets').get(id)
        return dataset


class DatasetSizeValidator(object):

    def __init__(self, dataset):
        self.size = dataset['size']

    def verify_size(self):
        if 'size' in dataset:
            if isinstance(self.size, int) and self.size > 0:
                return True
            else:
                raise "Size must be integer and higher than 0"
        else:
            raise "Dont Found Size"


class DatasetFormatValidator(object):

    def __init__(self, dataset):
        self.format = dataset["format"]
        self.format_header = self.format["header"]
        self.format_type = self.format["type"]

    def verify_format(self):
        if 'format' in dataset:
            if 'header' in self.format:
                if isinstance(self.format_header, bool):
                    return True
                else:
                    raise "Format Header must be boolean"
            else:
                raise "Dont Found Header"
            if 'type' in self.format:
                if isinstance(self.format_type, str):
                    return True
                else:
                    raise "Format Type must be csv or json"
            else:
                raise "Dont Found Type"
        else:
            raise "Dont Found Format"


class DatasetFieldsValidator(object):

    def __init__(self, dataset):
        self.field = dataset["fields"]

    def verify_fields(self):
        if 'fields' in dataset:
            for body_field in self.field:
                if 'name' in body_field:
                    self.name = body_field.get('name')
                    if isinstance(self.name, str):
                        return True
                    else:
                        raise "Name type must be string"
                else:
                    raise "Dont Found Name in Fields"
                if 'generator' in body_field:
                    self.generator = body_field.get('generator')
                    if isinstance(self.generator, dict):
                        return True
                    else:
                        raise "Generator must be dict"
                else:
                    raise "Dont Found Generator in Fields"
                if 'type' in body_field:
                    self.type = body_field.get('type')
                    if isinstance(self.type, (str, bool, float, int, list)):
                        return True
                    else:
                        raise "Type is not "
                else:
                    raise "Dont Found Type in Fields"
        else:
            raise "Fields Dont Exist in Dataset"


class DatasetSerializerValidator(object):

    def __init__(self, dataset):
        self.serializers = dataset["serializers"]
        self.to = self.serializers["to"]

    def verify_serializers(self):
        if 'to' in self.serializers:
            for dict_to in self.to:
                if 'type' in dict_to:
                    self.type = dict_to.get('type')
                    if isinstance(self.type, str):
                        return True
                    else:
                        raise "Serializer type must be string"
                else:
                    raise "Dont Found Type in Serializers"
                if 'uri' in dict_to:
                    self.to = dict_to.get('uri')
                    if isinstance(self.to, str):
                        return True
                    else:
                        raise "uri error"
                else:
                    raise "Dont Found uri in Serializers"


if __name__ == "__main__":

    spec = Dataset("fake_generator_sample.txt")
    dataset = spec.get_parameters()
    size_validator = DatasetSizeValidator(dataset)
    format_validator = DatasetFormatValidator(dataset)
    field_validator = DatasetFieldsValidator(dataset)
    serializer_validator = DatasetSerializerValidator(dataset)

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
