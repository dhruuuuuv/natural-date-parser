import json
import os
import dateparser as dp
import datetime
from dataclasses import dataclass, field
from typing import Any, List
from text2digits import text2digits

list_of_natural_date_ranges = [
    'yesterday',
    'last week',
    'last month',
    'last year',
    '1 week ago',
    'one week ago',
    '2 hours ago',
    'day before yesterday',
    'five hours ago',
    'last year',
    'next tuesday',
    'next week',
    'following week',
    'manaña',
    'in one week',
    'pineapple',
    '6th feb 2018',
    '02-04-1995 to 01-05-1995'
]

DATE_FORMAT = '%H:%M:%S on %d-%m-%y'


@dataclass
class DateParser:
    dates: List
    today: datetime.datetime

    def parse_dates(self):
        if type(self.dates) is not list:
            self.dates = [ self.dates ]

        for date in self.dates:
            t2d = text2digits.Text2Digits()
            text_with_integers = t2d.convert(date)
            parsed = self.parse_single_date(text_with_integers)
            if parsed is None:
                #     try other methods
                print('{}: Unable to parse date'.format(date))
            else:
                # if date.date() != self.today.date():

                print('{}: {}'.format(date, self.compare_dates(parsed)))

    @staticmethod
    def parse_single_date(date):
        parsed_date = dp.parse(date)
        return parsed_date

    def compare_dates(self, date):
        from_date = ''
        to_date = ''
        if date < self.today:
            from_date = self.format_date(date)
            to_date = self.format_date(self.today)
        else:
            from_date = self.format_date(self.today)
            to_date = self.format_date(date)
        output_str = 'from {from_date} to {to_date}'.format(from_date=from_date, to_date=to_date)
        return output_str

    @staticmethod
    def format_date(date):
        if date is None:
            return None
        else:
            formatted = date.strftime(DATE_FORMAT)
            return formatted


if __name__ == '__main__':
    parser = DateParser(list_of_natural_date_ranges, datetime.datetime.now())
    parser.parse_dates()

