from data_manager import DataManager
from reports.report import Report


class AnnualMinMaxReport(Report):
    def __init__(self, data_store: DataManager) -> None:
        super().__init__(data_store)

    def printReport(self):
        print("{:<10} {:<12} {:<12} {:<15} {:<12}".format(
            'Year', 'MAX Temp', 'MIN Temp', 'MAX Humidity', 'MIN Humidity'))
        sortedYears = self.data_store.sortedYears()

        for year in sortedYears:
            year = self.data_store.years[year]
            max_temperature = year.max_temperature()
            min_temperature = year.min_temperature()
            max_humidity = year.max_humidity()
            min_humidity = year.min_humidity()

            print("{:<10} {:<12} {:<12} {:<15} {:<12}".format(
                year.year, max_temperature, min_temperature, max_humidity, min_humidity))
