from click.testing import CliRunner

from src.cli.commands import execute
from src.generators.handler import GeneratorsHandler


class TestCliExecutor:
    def test_cli_executor_file(self, mocker):
        mock = mocker.patch.object(GeneratorsHandler, 'generate')
        mock_ = mocker.patch.object(GeneratorsHandler,
                                    'get_valid_specification')
        mock.return_value = [("a", "b", "c",)]
        mock_.return_value = {}
        runner = CliRunner()
        with runner.isolated_filesystem():
            with open('hello.json', 'w') as f:
                f.write("{{}}")
                result = runner.invoke(execute, ['generate', 'hello.json'])
                assert result.exit_code == 0
