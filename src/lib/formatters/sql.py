

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
            mode = options.get("mode")
            fields = options.get("schema")
            types_fields = options.get(fields)
            mode = options.get("mode")
            if mode not in ["append", "replace", "truncate", "", None]:
                raise ValueError(
                                "SQL suports only 'append', \
                                'replace' and 'truncate' ")
            if mode == "replace" and types_fields not in ["sqltype", "quoted"]:
                raise ValueError(
                        "Schema fields suports only 'sqltype' and 'quoted'")
        return {
            'required': {
                'options.table_name': {'none': False, 'type': str},
                'options.mode': {'none': False, 'type': str},
                'options.schema': {'none': False, 'type': dict},
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

    @staticmethod
    def check(options):
        
        mode = options.get("mode")
        if mode in ["append", "replace", "truncate", "", None]:
            pass
        else:
            raise ValueError(
                            "SQL suports only 'append', \
                            'replace' and 'truncate' ")
