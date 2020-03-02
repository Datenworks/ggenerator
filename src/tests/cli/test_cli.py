import os

from click.testing import CliRunner

from src.cli.commands import execute
from src.generators.handler import GeneratorsHandler
from src.tests.cli.cli_fixture import *  # noqa: F403, F401


class TestCliExecutor:
    def test_cli_executor_file(self, mocker, generate_files):
        runner = CliRunner()
        mock = mocker.patch.object(GeneratorsHandler, 'generate')
        mock.return_value = [("a", "b", "c")]
        mock_ = mocker.patch.object(GeneratorsHandler,
                                    'valid_specification_dataset')
        mock_.return_value = {}

        with runner.isolated_filesystem():
            with open('hello.json', 'w') as f:
                f.write("{{}}")
            result = runner.invoke(execute, ['generate',
                                             '--spec',
                                             'hello.json'])
            assert result.exit_code == 0

    def test_cli_executor_folder(self, mocker, generate_files):
        runner = CliRunner()
        mock = mocker.patch.object(GeneratorsHandler, 'generate')
        mock.return_value = [("a", "b", "c")]
        mock_ = mocker.patch.object(GeneratorsHandler,
                                    'valid_specification_dataset')
        mock_.return_value = {}

        with runner.isolated_filesystem():
            os.mkdir('dir/')
            result = runner.invoke(execute, ['generate',
                                             '--spec',
                                             'dir/'])
            assert result.exit_code != 0

    def test_cli_executor_file_not_found(self, mocker, generate_files):
        runner = CliRunner()
        mock = mocker.patch.object(GeneratorsHandler, 'generate')
        mock.return_value = [("a", "b", "c")]
        mock_ = mocker.patch.object(GeneratorsHandler,
                                    'valid_specification_dataset')
        mock_.return_value = {}

        with runner.isolated_filesystem():
            result = runner.invoke(execute, ['generate',
                                             '--spec',
                                             'hello.json'])
            assert result.exit_code != 0
