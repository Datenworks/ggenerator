import json

from src.lib.formatters import formatters
from src.generators.datatypes import get_generators_map
from src.lib.writers import writers, uri_writers
from functools import reduce

generators_map = get_generators_map()


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

    def __init__(self, id, size, locale, fields, format, serializers):
        self.id = id
        self.size = size
        self.locale = locale
        self.fields = fields
        self.format = format
        self.serializers = serializers

        self.format_validator = ConfigurationFormat(self.format)
        self.fields_validator = ConfigurationFields(self.fields)
        self.serializer_validator = ConfigurationSerializer(self.serializers,
                                                            self.id)

    def _valid_size(self):
        if self.size is not None and \
                isinstance(self.size, int) and \
                self.size > 0:
            return True
        else:
            raise ValueError("size must be int and bigger than 0")

    def _valid_locale(self):
        if self.locale is not None \
           and isinstance(self.locale, str) \
           and self.locale != "":
            return True
        else:
            raise ValueError("locale must not be empty/none")

    def _valid_fields(self):
        if self.fields is not None and \
                isinstance(self.fields, list) and \
                len(self.fields) > 0:
            return True
        else:
            raise ValueError("fields must be a list and bigger than 0")

    def _valid_format(self):
        if self.format is not None and \
                len(self.format) > 0:
            return True
        else:
            raise ValueError("format must not be empty/none")

    def _valid_serializers(self):
        if self.serializers is not None and \
                len(self.serializers) > 0:
            return True
        else:
            raise ValueError("serializers must not be empty/none")

    def is_valid(self):
        has_id = self.id is not None
        has_size = self._valid_size()
        has_locale = self._valid_locale()
        has_fields = self._valid_fields()
        has_format = self._valid_format()
        has_serializers = self._valid_serializers()

        if not (has_id and has_size and
                has_fields and has_format and
                has_serializers and has_locale):
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
        if self.format is None:
            return False

        if 'type' not in self.format:
            return False
        json_array_type = self.format.get("type")

        if json_array_type == "json-array":
            if 'options' in self.format:
                indent = self.format.get('options').get("indent")
                type_of_indent = self.validade_typeof_indent_jsonarray(indent)
                is_valid = self.validate_jsonarray_format(type_of_indent)
                return is_valid
            return True
        else:
            format_type = self.format.get("type")
            has_format_type = format_type is not None and \
                isinstance(format_type, str) and \
                format_type in formatters
            is_valid = has_format_type
            return is_valid

    def validade_typeof_indent_jsonarray(self, indent):
        rules = [
            "pretty",
            "minify",
            "",
            None
        ]
        if indent in rules:
            format_type = self.format.get("type")
            return format_type
        else:
            raise ValueError(
                            "json-array suports only 'pretty' and 'minify'")

    def validate_jsonarray_format(self, format_type):
        has_format_type = format_type is not None and \
            isinstance(format_type, str) and \
            format_type in formatters
        is_valid = has_format_type
        return is_valid


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
