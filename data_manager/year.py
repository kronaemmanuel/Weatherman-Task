from data_manager.day import Day
from data_manager.month import Month


class Year:
    def __init__(self, year: int) -> None:
        self.year: int = year
        self.months: list[Month] = []

    def addMonth(self, month: Month):
        self.months.append(month)

    def max_temperature_day(self) -> Day:
        return max([month.max_temperature_day() for month in self.months], key=lambda day: day.max_temperature)

    def min_temperature_day(self) -> Day:
        return min([month.min_temperature_day() for month in self.months], key=lambda day: day.min_temperature)

    def max_humidity_day(self) -> Day:
        return max([month.max_humidity_day() for month in self.months], key=lambda day: day.max_humidity)

    def min_humidity_day(self) -> Day:
        return min([month.min_humidity_day() for month in self.months], key=lambda day: day.min_humidity)
