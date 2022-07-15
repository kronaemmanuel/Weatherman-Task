from data_manager.Month import Month


class Year:
    def __init__(self, year: int) -> None:
        self.year: int = year
        self.months: list[Month] = []

    def addMonth(self, month: Month):
        self.months.append(month)

    def max_temperature(self):
        return max([month.max_temperature() for month in self.months])

    def min_temperature(self):
        return min([month.min_temperature() for month in self.months])

    def max_humidity(self):
        return max([month.max_humidity() for month in self.months])

    def min_humidity(self):
        return min([month.min_humidity() for month in self.months])
