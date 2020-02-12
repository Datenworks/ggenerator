from dateutil.parser import parse
from datetime import datetime
from generator.datatypes.float import FloatType


class TimestampType:
    def __init__(self, start_at: str, end_at: str):
        self.start_date = start_at
        self.end_date = end_at
        self.float_gen = FloatType

    def __get_epoch_of_iso(self, iso_date):
        return parse(iso_date).timestamp()

    def __generate_between_epochs(self, start_epoch,
                                  end_epoch, num_of_records):
        generated_epochs = self.float_gen(start_at=start_epoch,
                                          end_at=end_epoch)\
            .generate(num_of_records)
        return [datetime.fromtimestamp(epoch).isoformat()
                for epoch in generated_epochs]

    def generate(self, num_of_records) -> list:
        start_epoch = self.__get_epoch_of_iso(self.start_date)
        end_epoch = self.__get_epoch_of_iso(self.end_date)
        return self.__generate_between_epochs(start_epoch,
                                              end_epoch,
                                              num_of_records)
