from tkinter import W
from data_manager.Day import Day


class Month:
    def __init__(self, month: int) -> None:
        self.month: int = month
        self.days: list[Day] = []
        self.max_temperature_day_index: int = 0
        self.min_temperature_day_index: int = 0
        self.max_humidity_day_index: int = 0
        self.min_humidity_day_index: int = 0

    def addDay(self, new_day: Day):
        self.days.append(new_day)
        new_day_index = len(self.days) - 1

        if new_day.max_temperature > self.days[self.max_temperature_day_index].max_temperature:
            self.max_temperature_day_index = new_day_index

        if new_day.min_temperature < self.days[self.min_temperature_day_index].min_temperature:
            self.min_temperature_day_index = new_day_index

        if new_day.max_humidity > self.days[self.max_humidity_day_index].max_humidity:
            self.max_humidity_day_index = new_day_index

        if new_day.min_humidity < self.days[self.min_humidity_day_index].min_humidity:
            self.min_humidity_day_index = new_day_index

    def max_temperature_day(self) -> Day:
        return self.days[self.max_temperature_day_index]

    def min_temperature_day(self) -> Day:
        return self.days[self.min_temperature_day_index]

    def max_humidity_day(self) -> Day:
        return self.days[self.max_humidity_day_index]

    def min_humidity_day(self) -> Day:
        return self.days[self.min_humidity_day_index]
