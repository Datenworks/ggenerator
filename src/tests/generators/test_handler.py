from pandas import DataFrame

from src.generators.handler import GeneratorsHandler
from src.tests.generators.handler_fixtures import simple_valid_specification


class TestGeneratorsHandler(object):
    """Unit-test of GeneratorsHandler class"""

    def test_simple_specification_dataframe(self,
                                            mocker,
                                            simple_valid_specification):
        mock = mocker.patch \
                     .object(GeneratorsHandler, 'get_valid_specification')
        mock.return_value = simple_valid_specification
        handler = GeneratorsHandler({'config_file': None})
        dataframe = handler.generate_dataframe()

        assert isinstance(dataframe, DataFrame) is True
