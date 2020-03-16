import random
import time


class SmoothRandom():
    def __init__(self, lower_limit: int, upper_limit: int, variance: int, start=None, seed=None):
        self.lower = lower_limit
        self.upper = upper_limit
        self.variance = variance
        self.n = start if start is not None else (self.lower+self.upper)//2
        random.seed(a=seed)

    def __iter__(self):
        return self

    def __next__(self):
        next_val = random.randint(-self.variance, self.variance)
        next_next_val = random.randint(-self.variance, self.variance)
        self.n = min(
            max(self.n + next_val + next_next_val, self.lower), self.upper)
        return self.n


if __name__ == '__main__':
    my_rand = SmoothRandom(50, 150, 1)
    for i in my_rand:
        print('\r', i, '      ', end='')
        time.sleep(0.1)
