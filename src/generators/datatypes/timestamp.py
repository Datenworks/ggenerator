from dateutil.parser import parse
from datetime import datetime
from random import randrange
from datetime import timedelta
import pytz


class TimestampType:
    key = 'timestamp'

    def __init__(self, start_at: str = "1970-01-01T00:00:00UTC",
                 end_at: str = datetime.now(tz=pytz.UTC).isoformat(),
                 tz: str = "UTC"):
        self.start_date = self.__parse_to_datetime(start_at)
        self.end_date = self.__parse_to_datetime(end_at)
        self.time_zone = pytz.timezone(tz)

    def generate(self) -> datetime:
        return self.__generate_random_date(self.start_date,
                                           self.end_date)\
                   .replace(tzinfo=self.time_zone)

    def __parse_to_datetime(self, iso_format_date) -> datetime:
        return parse(iso_format_date)

    def __generate_random_date(self, start, end) -> datetime:
        """
        This function will return a random datetime between two datetime
        objects.
        """

        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    def generate_records(self, num_of_records) -> list:
        return [self.generate() for _ in range(num_of_records)]
