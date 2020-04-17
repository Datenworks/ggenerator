from src.lib.writers import writers, database_writers


class SerializersConfiguration(object):

    @staticmethod
    def get_database_type(serializer):
        options = serializer.get('options', {})
        engine = options.get('engine')
        method = options.get('method')
        return f"{engine}-{method}"

    @staticmethod
    def get_rules(serializer):
        type_ = serializer.get('type')

        if type_ not in writers:
            type_ = SerializersConfiguration.get_database_type(serializer)
            if type_ not in database_writers:
                raise ValueError(f"Serializer type `{type_}` not found")

        type_class = writers.get(type_)

        return type_class.rules()
