from data_manager.Day import Day
from data_manager.Month import Month


class Year:
    def __init__(self, year: int) -> None:
        self.year: int = year
        self.months: list[Month] = []

    def addMonth(self, month: Month):
        self.months.append(month)

    def max_temperature(self) -> int:
        return max([month.max_temperature() for month in self.months])

    def min_temperature(self) -> int:
        return min([month.min_temperature() for month in self.months])

    def max_humidity(self) -> int:
        return max([month.max_humidity() for month in self.months])

    def min_humidity(self) -> int:
        return min([month.min_humidity() for month in self.months])

    def hottest_day(self) -> Day:
        monthly_hottest_days = []
        for month in self.months:
            monthly_hottest_days.append(month.hottest_day())

        return max(monthly_hottest_days, key=lambda day: day.max_temperature)
