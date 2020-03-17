from src.lib.writers import writers


class SerializersConfiguration(object):

    @staticmethod
    def get_rules(serializer):
        type_ = serializer.get('type')

        if type_ not in writers:
            raise ValueError(f"Serializer type `{type_}` not found")

        type_class = writers.get(type_)

        return type_class.rules()
