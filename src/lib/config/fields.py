from src.generators.datatypes import Metadata


class FieldsConfiguration(object):

    @staticmethod
    def get_rules(field):
        type_ = field.get('type')
        metadata = Metadata('pt-BR')
        generators = metadata.get_generators_map()

        if type_ not in generators:
            raise ValueError(f"Field type `{type_}` not found")

        type_class = generators[type_]['type']

        return type_class.rules()
