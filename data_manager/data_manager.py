import csv
import re
import sys
from os import listdir
from os.path import isfile, join

import constants

from data_manager.day import Day
from data_manager.month import Month
from data_manager.year import Year

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


class DataManager:
    def __init__(self, base_path) -> None:
        self.years = {}
        self.base_path = base_path
        try:
            self.data_folder = [f for f in listdir(
                self.base_path) if isfile(join(self.base_path, f))]
        except:
            raise ValueError

    def import_data(self):
        for data_file in self.data_folder:
            with open(join(self.base_path, data_file), newline='') as data_file:
                year_number = int(re.search(r'\d{4}', data_file.name).group())

                if year_number not in self.years.keys():
                    self.years[year_number] = Year(year_number)

                year = self.years[year_number]

                month_name = data_file.name[-7:-4]
                month_number = MONTHS.index(month_name) + 1
                month = Month(month_number)

                reader = csv.reader(data_file)
                month_data = []
                for row in reader:
                    month_data.append(row)

                # Remove first two lines and last line
                month_data = month_data[2:-1]

                for row in month_data:
                    try:
                        if any(row[key] in (None, '') for key in [0, 1, 3, 7, 9]):
                            raise ValueError

                        day_number = int(
                            re.search(r'\d{1,2}$', row[0]).group())
                        max_temperature = int(row[1])
                        min_temperature = int(row[3])
                        max_humidity = int(row[7])
                        min_humidity = int(row[9])

                        if day_number not in range(1, 31):
                            raise ValueError

                        day = Day(day_number, month_number, year_number, max_temperature,
                                  min_temperature, max_humidity, min_humidity)

                        month.addDay(day)
                    except:
                        if constants.debug_mode:
                            print("Ignoring Data Row: Invalid Data",
                                  sys.exc_info()[0])

                # Add month if it has data for at least one day
                if len(month.days) > 0:
                    year.addMonth(month)

    def printData(self):
        for year in self.years:
            year = self.years[year]
            for month in year.months:
                for day in month.days:
                    print(year.year, month.month, day.day)

    def sortedYears(self):
        return sorted(self.years)

    def getYear(self, year_number: int) -> Year:
        return self.years[year_number]
