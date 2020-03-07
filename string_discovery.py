import random
import string
import random

class Simulation:
    """Simulate biosphere"""
    goal: str

    def __init__(self, goal: str, pop_size: int):
        self.goal = goal
        self.gen = 0
        self.pop_size = pop_size


    def first_string(self, size: int) -> str:
        """Generates a random string of 'abcdefghijklmnopqrstuvwxyz '."""
        letters = string.ascii_lowercase + ' '
        return ''.join(random.choice(letters) for _ in range(size))

    def begin_sim(self, goal: str) -> None:
        first = self.first_string(len(self.goal))
        while()

if __name__ == '__main__':
    print('Enter a lower case sentence:')
    inp = input()
    while isinstance(inp, str):
        print('Invalid input, try again:')
        inp = input()
