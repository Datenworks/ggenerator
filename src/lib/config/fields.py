from src.generators.datatypes import get_generators_map


class FieldsConfiguration(object):

    @staticmethod
    def get_rules(field):
        type_ = field.get('type')
        generators = get_generators_map()

        if type_ not in generators:
            raise ValueError(f"Field type `{type_}` not found")

        type_class = generators.get(type_)

        return type_class.rules()
