class Day_of_wee_iterator:
    def __init__(self):
        self.current_day = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current_day
        self.current_day = (self.current_day + 1) % 7
        return result


# Przykład użycia
iterator = Day_of_wee_iterator()
for _ in range(20):
    print(next(iterator))
