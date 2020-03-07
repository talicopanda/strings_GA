import random
import string
import random

from Population import Population


class Simulation:
    """Simulate biosphere"""
    goal: str

    def __init__(self, goal: str, pop_size: int):
        self.goal = goal
        self.gen = 1
        self.pop_size = pop_size


    def first_string(self, size: int) -> str:
        """Generates a random string of 'abcdefghijklmnopqrstuvwxyz '."""
        letters = string.ascii_lowercase + ' '
        return ''.join(random.choice(letters) for _ in range(size))

    def begin_sim(self) -> None:
        current = self.first_string(len(self.goal))
        while current != self.goal:
            self.gen += 1
            new_pop = Population(current, self.pop_size, self.gen)
            current = new_pop.fittest()
            print(current)

if __name__ == '__main__':
    print('Enter a lower case sentence:')
    goal = input()
    while isinstance(goal, str):
        print('Invalid input, try again:')
        goal = input()
    print('Enter a population size:')
    pop_size = input()
    while isinstance(pop_size, int):
        print('Invalid input, try again:')
        pop_size = input()
    my_sim = Simulation(goal, pop_size)
    my_sim.begin_sim()
