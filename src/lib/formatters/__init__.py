from src.lib.formatters.csv import CsvFormatter
from src.lib.formatters.json import JsonFormatter

formatters = {
    CsvFormatter.key: CsvFormatter,
    JsonFormatter.key: JsonFormatter
}
