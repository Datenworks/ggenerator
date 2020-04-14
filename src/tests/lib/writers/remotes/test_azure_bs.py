from src.lib.writers.remotes.azure_bs import AzureBlobStorage
from src.lib.formatters import formatters
from src.tests.lib.writers.remotes.fixtures import *  # noqa: F403, F401
import os
import pytest


class TestAzureBSWriter(object):
    def tes__azure_without_connection_string(self,
                                             mocker,
                                             specification_azure_bs):
        csv_formatter = formatters['csv']({"options": {"header": True}})
        mock = mocker.patch.object(os, 'getenv')
        mock.return_value = None

        with pytest.raises(Exception):
            AzureBlobStorage(formatter=csv_formatter,
                             specification=specification_azure_bs)
