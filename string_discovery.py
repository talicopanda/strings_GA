import random
import string
import random

from Population import Population
from String import String


class Simulation:
    """Simulate biosphere"""
    goal: str

    def __init__(self, goal: str, pop_size: int):
        self.goal = goal
        self.gen = 1
        self.pop_size = pop_size


    def first_string(self) -> String:
        """Generates a random string of 'abcdefghijklmnopqrstuvwxyz '."""
        letters = string.ascii_lowercase + ' '
        return String(''.join(random.choice(letters) for _ in range(len(goal))), goal)

    def begin_sim(self) -> None:
        current = self.first_string()
        print(current)
        while current.content != self.goal:
            self.gen += 1
            new_pop = Population(current, self.pop_size, self.gen, self.goal)
            new_pop.generate_pop()
            current = new_pop.fittest()
            print(current)

if __name__ == '__main__':
    print('Enter a lower case sentence:')
    goal = input()
    while not isinstance(goal, str):
        print('Invalid input, try again:')
        goal = input()
    print('Enter a population size:')
    pop_size = int(input())
    my_sim = Simulation(goal, pop_size)
    my_sim.begin_sim()
    print(f"Total Generations: {my_sim.gen}")
    print(f"Total Strings Generated: {my_sim.gen*pop_size}")
