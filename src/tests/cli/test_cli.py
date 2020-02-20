from click.testing import CliRunner
from src.cli.commands import execute


class TestCliExecutor:
    def test_cli_executor_file(self, mocker):
        runner = CliRunner()
        mock = mocker.patch.Object()
        result = runner.invoke(['spec_path'])
        assert result.exit_code == 0
