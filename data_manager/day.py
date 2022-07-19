class Day:
    def __init__(self, day: int, month: int, year: int, max_temperature: int, min_temperature: int, max_humidity: int, min_humidity: int) -> None:
        self.day: int = day
        self.month: int = month
        self.year: int = year
        self.max_temperature: int = max_temperature
        self.min_temperature: int = min_temperature
        self.max_humidity: int = max_humidity
        self.min_humidity: int = min_humidity

    def get_date(self) -> str:
        return f"{self.day}/{self.month}/{self.year}"
