class Day:
    def __init__(self, day: int, max_temperature: int, min_temperature: int, max_humidity: int, min_humidity: int) -> None:
        self.day: int = day
        self.max_temperature: int = max_temperature
        self.min_temperature: int = min_temperature
        self.max_humidity: int = max_humidity
        self.min_humidity: int = min_humidity
