import random


class N_E_S_W_iterator:
    DIRECTIONS = ["N", "E", "S", "W"]

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(self.DIRECTIONS)


# Przykład użycia
iterator = N_E_S_W_iterator()
for _ in range(20):
    print(next(iterator))
