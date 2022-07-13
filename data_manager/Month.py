from data_manager.Day import Day


class Month:
    def __init__(self, month: int) -> None:
        self.month: int = month
        self.days: list[Day] = []

    def addDay(self, day: Day):
        self.days.append(day)
