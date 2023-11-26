import random


class RandomDirectionIterator:
    DIRECTIONS = ["N", "E", "S", "W"]

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(self.DIRECTIONS)


# Przykład użycia
random_direction_iterator = RandomDirectionIterator()
for _ in range(20):
    print(next(random_direction_iterator))
