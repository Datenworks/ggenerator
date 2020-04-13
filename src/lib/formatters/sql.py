

class SqlFormatter(object):
    """Class that receive pandas dataframe
    and write it down in Sql format
    """
    key = 'sql'

    def __init__(self, specification={}):
        self.default = {'index': False, 'batch_size': 50, "mode": "append"}
        self.specification = specification

    @staticmethod
    def rules():
        def replace_rule(options):
            schema = options.get("schema")
            for key in schema.keys():
                field = schema.get(key)
                mode = options.get("mode")
                if mode == "replace":
                    if not isinstance(field.get("sqltype", None), str):
                        raise ValueError(
                            "The Mode replace needs'sqltype' in Schema fields")

        def quoted_rule(schema):
            for key in schema.keys():
                field = schema.get(key)
                if not isinstance(field.get("quoted", None), bool):
                    raise ValueError(" Schema fields required 'quoted'")

        return {
            'required': {
                'options.table_name': {'none': False, 'type': str},
                'options.mode': {'none': False,
                                 'type': str,
                                 'values': ["append", "replace", "truncate"]},
                'options.schema': {'none': False,
                                   'type': dict,
                                   'custom': [quoted_rule]},
                'options': {'none': False,
                            'type': dict,
                            'custom': [replace_rule]}
            },
            'optional': {
                'options.batch_size': {'none': False, 'type': int},
                'options.index': {'none': False, 'type': bool},
                'options.index_label': {'none': False, 'type': str},
            }
        }
