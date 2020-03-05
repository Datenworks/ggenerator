import json

from src.lib.formatters import formatters
from src.generators.datatypes import generators_map
from src.lib.writers import writers, uri_writers
from functools import reduce


class ConfigurationValidator(object):

    def __init__(self, file_path):
        self.file_path = file_path

    def get_config(self):

        file = open(self.file_path, 'r')
        try:
            configuration = json.loads(file.read())
        except ValueError:
            raise ValueError("Malformed specification file/blank field")
        else:
            file.close()
            return configuration


class ConfigurationDataset(object):

    def __init__(self, id, size, fields, format, serializers):
        self.id = id
        self.size = size
        self.fields = fields
        self.format = format
        self.serializers = serializers

        self.format_validator = ConfigurationFormat(self.format)
        self.fields_validator = ConfigurationFields(self.fields)
        self.serializer_validator = ConfigurationSerializer(self.serializers,
                                                            self.id)

    def is_valid(self):
        has_id = self.id is not None
        has_size = self.size is not None and \
            isinstance(self.size, int) and \
            self.size > 0
        has_fields = self.fields is not None and \
            isinstance(self.fields, list) and \
            len(self.fields) > 0
        has_format = self.format is not None
        has_serializers = self.serializers is not None

        if not (has_id and has_size and
                has_fields and has_format and
                has_serializers):
            return False

        are_fields_valid = self.fields_validator.is_valid()
        is_format_valid = self.format_validator.is_valid()
        is_serializer_valid = self.serializer_validator.is_valid()

        is_valid = is_format_valid and \
            is_serializer_valid and \
            are_fields_valid
        return is_valid


class ConfigurationFormat(object):

    def __init__(self, format):
        self.format = format

    def is_valid(self):
        format_type = self.format.get("type")
        has_format_type = format_type is not None and \
            isinstance(format_type, str)

        return has_format_type and \
            format_type in formatters


class ConfigurationFields(object):

    def __init__(self, fields):
        self.fields = fields

    def is_valid(self):
        for field in self.fields:
            if self.__is_valid_field(field) is False:
                return False
            if self.__generator_type_is_valid(field) is False:
                return False
        return True

    def __is_valid_type(self, field):
        field_type = field.get("type")
        generator = field.get("generator")

        if field_type not in generators_map:
            return False

        clazz = generators_map[field_type]['type']
        return clazz.check(generator)

    def __is_valid_field(self, field):
        name = field.get("name")
        has_name = name is not None and isinstance(name, str)
        field_type = field.get("type")
        has_field_type = field_type is not None and isinstance(field_type, str)

        generator = field.get("generator")
        if generator is None or not isinstance(generator, dict):
            return False

        is_valid_type = self.__is_valid_type(field)
        is_valid = has_name and has_field_type and is_valid_type

        return is_valid

    def __generator_type_is_valid(self, field):
        generator = field.get("generator", {})
        field_type = field.get("type")
        type_ = generators_map[field_type]
        if not generator and type_['generator']['optional']:
            return True
        if generator:
            arguments = generator.keys()
            type_ = generators_map[field_type]
            return all([arg in type_['generator']['arguments']
                        for arg in arguments])
        return False


class ConfigurationSerializer(object):

    def __init__(self, serializers, dataset_id):
        self.dataset_id = dataset_id
        self.serializers = serializers

    def is_valid(self):
        to = self.serializers.get('to')
        serializer_to = to is not None and isinstance(to, list)
        if serializer_to is True:
            return self.__is_valid_output(to)
        return False

    def __is_valid_output(self, to):
        for output in to:
            output_type = output.get("type")
            output_uri = output.get("uri")
            is_valid_type = self.__has_valid_type(output_type)

            if not output_uri and output_type in uri_writers:
                output.update({"uri": self.__get_uri_from_user(output_type)})

            is_valid_destination = \
                self.__has_valid_destination(output_type, **output)

            verify_output_type = output_type is not None and \
                isinstance(output_type, str)
            writer = writers.get(output_type)

            is_valid = is_valid_type and is_valid_destination \
                and verify_output_type and writer is not None

            if is_valid is False:
                return False
        return True

    def __has_valid_type(self, output_type):
        if output_type is not None and\
                    isinstance(output_type, str)\
                    and output_type in writers:
            return True
        else:
            msg_writers = reduce(lambda a, b: a + " | " + b,
                                 writers.keys(), '')
            message = f"Please, insert a valid destination type: {msg_writers}"
            raise Exception(message)

    def __has_valid_destination(self, output_type, **kwargs):
        return writers[output_type].is_valid_destination(**kwargs)

    def __get_uri_from_user(self, output_type):
        from src.cli.commands import get_uri
        return get_uri(dataset_name=self.dataset_id, output_type=output_type)
