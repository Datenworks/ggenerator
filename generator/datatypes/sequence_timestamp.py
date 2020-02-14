from dateutil.parser import parse
from datetime import datetime
from datetime import timedelta
from pandas import date_range
import pytz


class TimestampSequenceType:
    def __init__(self, start_at: str = "1970-01-01T00:00:01",
                 datepart: str = "second", tz: str = "UTC"):
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
        return parse(iso_format_date)

    def __generate_next(self, delta) -> datetime:
        return self.start_date + self.__delta_step(delta)

    def __delta_step(self, delta):
        return timedelta(seconds=self.datepart_in_seconds[self.datepart] * delta)

    def generate_records(self, num_of_records) -> list:
        return [self.__generate_next(delta)
                for delta in range(0, num_of_records)]
