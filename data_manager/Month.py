from data_manager.Day import Day


class Month:
    def __init__(self, month: int) -> None:
        self.month: int = month
        self.days: list[Day] = []

    def addDay(self, day: Day):
        self.days.append(day)

    def max_temperature(self) -> int:
        return max([day.max_temperature for day in self.days])

    def min_temperature(self) -> int:
        return min([day.min_temperature for day in self.days])

    def max_humidity(self) -> int:
        return max([day.max_humidity for day in self.days])

    def min_humidity(self) -> int:
        return min([day.min_humidity for day in self.days])

    def hottest_day(self) -> int:
        return max(self.days, key=lambda day: day.max_temperature)
