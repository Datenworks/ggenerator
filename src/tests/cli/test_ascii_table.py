from src.tests.generators.handler_fixtures import *  # noqa: F403, F401
from src.cli.ascii_table import print_asciiTable


class AsciiTester(object):
    def test_ascii_table(self, valid_specification):
        print_asciiTable(valid_specification)
