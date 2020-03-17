import pytz

from datetime import datetime
from dateutil.parser import isoparse
from datetime import timedelta


class TimestampSequenceType:
    key = 'timestamp:sequence'
    namespace = 'basic_type'
    optional_arguments = False

    def __init__(self, start_at: str,
                 datepart: str = "second", tz: str = "UTC",
                 *args, **kwargs):
        """
        step must be
        second | minute | hour | day | month | year
        default: second
        """
        self.start_date = self.__parse_to_datetime(start_at)
        self.datepart = datepart
        self.datepart_in_seconds = {
            "year": 365.25*24*60*60,
            "month": 365.25/12*24*60*60,
            "day": 24*60*60,
            "hour": 60*60,
            "minute": 60,
            "second": 1
        }
        self.time_zone = pytz.timezone(tz)

    def __parse_to_datetime(self, iso_format_date) -> datetime:
        return isoparse(iso_format_date)

    def __generate_next(self, delta) -> datetime:
        return self.start_date + self.__delta_step(delta)

    def __delta_step(self, delta):
        seconds = self.datepart_in_seconds[self.datepart]
        return timedelta(seconds=seconds * delta)

    @staticmethod
    def rules():
        def validate(value):
            try:
                isoparse(value)
            except ValueError:
                raise ValueError(f"Timestamp field `{value}` "
                                 "has a wrong format")
        return {'required': {'generator.start_at': {
                                'none': False,
                                'type': str,
                                'custom': [validate]}},
                'optional': {}}

    @staticmethod
    def sample():
        from random import randrange

        start = isoparse("1970-01-01T00:00:00Z").replace(tzinfo=pytz.UTC)
        end = isoparse("2019-01-01T00:00:00Z").replace(tzinfo=pytz.UTC)
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        date = (start + timedelta(seconds=random_second))
        date2 = (start + timedelta(seconds=random_second + 1))
        return [date, date2]

    def generate_records(self, num_of_records) -> list:
        return [self.__generate_next(delta)
                for delta in range(0, num_of_records)]
