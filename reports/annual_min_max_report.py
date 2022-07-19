from data_manager.data_manager import DataManager
from data_manager.day import Day
from data_manager.year import Year

from reports.report import Report


class AnnualMinMaxReport(Report):
    def __init__(self, data_store: DataManager) -> None:
        super().__init__(data_store)

    def printReport(self):
        print("{:<10} {:<12} {:<12} {:<15} {:<12}".format(
            'Year', 'MAX Temp', 'MIN Temp', 'MAX Humidity', 'MIN Humidity'))
        print("-----------------------------------------------------------------")
        sortedYears = self.data_store.sortedYears()

        for year in sortedYears:
            year: Year = self.data_store.years[year]
            max_temperature: int = year.max_temperature_day().max_temperature
            min_temperature: int = year.min_temperature_day().min_temperature
            max_humidity: int = year.max_humidity_day().max_humidity
            min_humidity: int = year.min_humidity_day().min_humidity

            print("{:<10} {:<12} {:<12} {:<15} {:<12}".format(
                year.year, max_temperature, min_temperature, max_humidity, min_humidity))
