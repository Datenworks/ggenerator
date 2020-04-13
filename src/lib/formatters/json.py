from pandas import DataFrame


class JsonFormatter(object):
    """Class that receive pandas dataframe
    and write it down in Json format
    """
    key = 'json-array'

    def __init__(self, specification={}):
        self.default = {'orient': 'records',
                        'date_unit': 's'}
        self.specification = specification

    @staticmethod
    def rules():
        return {'required': {},
                'optional': {
                    'options.orient': {'none': False, 'type': str},
                    'options.index': {'none': False, 'type': bool}
                }}

    def format(self, dataframe: DataFrame, path_or_buffer) -> None:
        """Format dataframe to json.

        Keyword arguments:
         - dataframe - pandas.Dataframe: dataframe containing the records
        """
        parameters = self.default
        options = self.specification.get('options', {})
        options['indent'] = 2 if options.get("indent") == "pretty" else 0
        parameters.update(options)
        if dataframe.shape[0] > 0:
            dataframe.to_json(
                path_or_buf=path_or_buffer, force_ascii=False, **parameters)
