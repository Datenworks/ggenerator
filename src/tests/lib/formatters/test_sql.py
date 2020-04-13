from src.lib.formatters.sql import SqlFormatter
from src.tests.lib.formatters.fixtures import *  # noqa: F403, F401
import pytest


class TestSqlFormatter(object):

    def test_invalid_quoted(self, schema_quoted_error):
        Sql_writer = SqlFormatter(specification={})
        msg_quoted_error = Sql_writer.rules.quoted_rule(schema_quoted_error)
        with pytest.raises(ValueError) as e:
            msg_quoted_error
        assert str(e.value) == " Schema fields required 'quoted'"

    def test_invalid_sqltype(self, schema_sqltype_error):
        Sql_writer = SqlFormatter(specification={})
        msg_sqltype_error = Sql_writer.rules.quoted_rule(schema_sqltype_error)
        with pytest.raises(ValueError) as e:
            msg_sqltype_error
        assert str(e.value) == "The Mode replace needs'sqltype' in Schema fields"
