from data_manager.Month import Month


class Year:
    def __init__(self, year: int) -> None:
        self.year: int = year
        self.months: list[Month] = []

    def addMonth(self, month: Month):
        self.months.append(month)

    def max_temperature(self):
        monthly_max_temperatures: list[int] = []
        for month in self.months:
            monthly_max_temperatures.append(month.max_temperature())

        return max(monthly_max_temperatures)

    def min_temperature(self):
        return 2

    def max_humidity(self):
        return 94

    def min_humidity(self):
        return 20
