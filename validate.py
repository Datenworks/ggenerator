import json


class Specification(object):
    
    def archives(self, filepath):
        files = [open(filepath, 'r').read()]   
        for spec in files:
           self.parameters = json.loads(spec)
    def get_parameters(self):
        for id in self.parameters.get('datasets').keys():
            dataset = self.parameters.get('datasets').get(id)
            if 'size' in dataset:
                if isinstance(dataset.get('size'), int) and dataset.get('size') > 0:
                    self.size = dataset.get('size')
                else:
                    raise "Size must be integer and higher than 0"
            else:
                raise "Dont Found Size "
            if 'format' in dataset:
                if 'header' in dataset.get('format'):
                    if isinstance(dataset.get('format').get('header'), bool):
                        self.format_header = dataset.get('format').get('header')
                    else:
                        raise "Format Header must be boolean"
                else:
                    raise "Dont Found Header"
            else:
                raise "Dont Found Format"
            if 'format' in dataset:
                if 'type' in dataset.get('format'):
                    if dataset.get('format').get('type') == "csv" or "json":
                        self.format_type = dataset.get('format').get('type')
                    else:
                        raise "Format Type must be csv or json"
                else:
                    raise "Dont Found Type"
            else:
                raise "Dont Found Format"
            if 'fields' in dataset:
                self.field = dataset.get('fields')
                body = [list_field for list_field in self.field]
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
            if 'serializers' in dataset:
                if 'to' in dataset.get('serializers'):
                    self.serializer_to = dataset.get('serializers').get('to')
                    body_to = [list_to for list_to in self.serializer_to] 
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
                        
                       

spec = Specification()
spec.archives("fake_generator_sample.txt")
spec.get_parameters()

