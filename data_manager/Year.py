from data_manager.Month import Month


class Year:
    def __init__(self, year: int) -> None:
        self.year: int = year
        self.months: list[Month] = []

    def addMonth(self, month: Month):
        self.months.append(month)
