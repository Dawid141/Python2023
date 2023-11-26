class iterator_0_1:
    def __init__(self):
        self.current_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current_value
        self.current_value = 1 - self.current_value
        return result


# Przykład użycia
iterator = iterator_0_1()
for _ in range(20):
    print(next(iterator))
