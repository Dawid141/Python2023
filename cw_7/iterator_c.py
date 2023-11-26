class DayOfWeekIterator:
    def __init__(self):
        self.current_day = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current_day
        self.current_day = (self.current_day + 1) % 7
        return result


# Przykład użycia
day_of_week_iterator = DayOfWeekIterator()
for _ in range(20):
    print(next(day_of_week_iterator))
