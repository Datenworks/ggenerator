import pytz

from datetime import datetime, timedelta
from dateutil.parser import isoparse
from typing import List


class TimestampSequenceType:
    key = 'timestamp:sequence'
    namespace = 'basic_type'
    optional_arguments = False

    def __init__(self, start_at: str,
                 datepart: str = "second", tz: str = "UTC", step: int = 1):
        """
        step must be
        second | minute | hour | day | month | year
        default: second
        """
        self.start_date = self.__parse_to_datetime(start_at)
        self.datepart = datepart
        self.step = step
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
        return (self.start_date + self.__delta_step(delta))\
            .astimezone(tz=self.time_zone)

    def __delta_step(self, delta):
        seconds = self.datepart_in_seconds[self.datepart]
        return timedelta(seconds=seconds * delta * self.step)

    def generate(self, num_of_records: int = 5) -> List[str]:
        return [dt.isoformat()
                for dt in self.generate_records(num_of_records=num_of_records)]

    def generate_records(self,
                         num_of_records,
                         progress=None) -> List[datetime]:
        results = []
        for delta in range(0, num_of_records):
            results.append(self.__generate_next(delta))
            progress and progress()

        return results

    @staticmethod
    def rules():
        def validate(value):
            try:
                isoparse(value)
            except ValueError:
                raise ValueError(f"Timestamp field `{value}` "
                                 "has a wrong format")
        return {
            'required': {
                'generator.start_at': {
                    'none': False,
                    'type': str,
                    'custom': [validate]
                }
            },
            'optional': {}
        }
