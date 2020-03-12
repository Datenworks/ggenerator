from src.lib.formatters import formatters


class FormattersConfiguration(object):

    @staticmethod
    def get_rules(format):
        format_ = format
        type_ = format_.get('type')

        if type_ not in formatters:
            raise ValueError(f"Format type `{type_}` not found")

        type_class = formatters.get(type_)

        return type_class.rules()
