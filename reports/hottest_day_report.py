from data_manager.Day import Day
from reports.report import Report
from data_manager import DataManager


class HottestDayReport(Report):
    def __init__(self, data_store: DataManager) -> None:
        super().__init__(data_store)

    def printReport(self):
        print("{:<10} {:<12} {:<12}".format('Year', 'Date', 'Temp'))
        print("----------------------------")
        sorted_years = self.data_store.sortedYears()

        for year in sorted_years:
            year = self.data_store.years[year]
            hottest_day: Day = year.hottest_day()
            print("{:<10} {:<12} {:<12}".format(
                year.year, hottest_day.get_date(), hottest_day.max_temperature))
