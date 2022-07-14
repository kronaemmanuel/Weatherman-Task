from data_manager.Day import Day


class Month:
    def __init__(self, month: int) -> None:
        self.month: int = month
        self.days: list[Day] = []

    def addDay(self, day: Day):
        self.days.append(day)

    def max_temperature(self) -> int:
        daily_max_temperatures: int = []
        for day in self.days:
            daily_max_temperatures.append(day.max_temperature)

        try:
            max_temp = max(daily_max_temperatures)
            return max_temp
        except:
            print("Max temperature not found due to invalid data")
            return 0
