"""
Import data from given directory

Directory format must be as follows:
directory-name:
├── lahore_weather_YEAR_MONTH.txt
├── lahore_weather_2000_Jan.txt
├── ...
└── lahore_weather_2011_May.txt

- Sub-directories are not supported
- YEAR is a 4 digit string
- MONTH is a 3 character ISO string
- File extension may be .txt or .csv but it will be read as a csv file
- First line of the file is empty
- Second line contains the header
- Indexes(zero-base) of data in the CSV file are as follows:
    - Max Temperature: 1
    - Min Temperature: 3
    - Max Humidity: 7
    - Min Humidity: 9

Output will be a list of Year objects
"""
import sys
from os import listdir
from os.path import isfile, join
import re
from data_manager.Year import Year
from data_manager.Month import Month
from data_manager.Day import Day
import csv


MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


class DataManager:
    def __init__(self) -> None:
        self.years = {}

    def import_data(self, base_path: str):
        # get list of files from given directory
        data_files = [f for f in listdir(
            base_path) if isfile(join(base_path, f))]

        for data_file in data_files:
            with open(join(base_path, data_file), newline='') as data_file:
                year = int(re.search(r'\d{4}', data_file.name).group())

                if year == 2000:
                    pass

                if year not in self.years.keys():
                    self.years[year] = Year(year)

                year = self.years[year]

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

                        day = Day(day_number, max_temperature,
                                  min_temperature, max_humidity, min_humidity)

                        month.addDay(day)
                    except:
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
