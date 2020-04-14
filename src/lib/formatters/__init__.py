from src.lib.formatters.csv import CsvFormatter
from src.lib.formatters.json import JsonFormatter
from src.lib.formatters.sql import SQLFormatter

formatters = {
    CsvFormatter.key: CsvFormatter,
    JsonFormatter.key: JsonFormatter,
    SQLFormatter.key: SQLFormatter
}
