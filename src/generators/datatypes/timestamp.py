import pytz

from dateutil.parser import isoparse
from datetime import datetime, timedelta
from random import randrange


class TimestampType:
    key = 'timestamp'
    namespace = 'basic_type'
    optional_arguments = False

    def __init__(self, start_at: str,
                 end_at: str,
                 tz: str = "UTC",
                 *args, **kwargs):
        self.time_zone = pytz.timezone(tz)
        self.start_date = start_at
        self.end_date = end_at

    @staticmethod
    def check(generator):
        start_at = generator.get("start_at")
        end_at = generator.get("end_at")

        if start_at is None or end_at is None:
            return False

        try:
            start_at = isoparse(start_at)
            end_at = isoparse(end_at)

            return start_at < end_at
        except ValueError:
            return False

    @staticmethod
    def sample():
        start = isoparse("1970-01-01T00:00:00Z").replace(tzinfo=pytz.UTC)
        end = isoparse("2019-01-01T00:00:00Z").replace(tzinfo=pytz.UTC)
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return (start + timedelta(seconds=random_second))

    def generate(self) -> datetime:
        dt_start_at = self.__parse_to_datetime(self.start_date)
        dt_end_at = self.__parse_to_datetime(self.end_date)
        return self.__generate_random_date(dt_start_at,
                                           dt_end_at)\
                   .replace(tzinfo=self.time_zone)

    def __parse_to_datetime(self, iso_format_date) -> datetime:
        return isoparse(iso_format_date).replace(tzinfo=self.time_zone)

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
