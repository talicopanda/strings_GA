import random
from typing import List
import string

from String import String


class Population:
    """Creates a population based on mutation of a single element
    """
    parent: String
    pop_size: int
    population: List
    letters: str
    id: int

    def __init__(self, parent: String, pop_size: int, id: int, goal: str):
        self.parent = parent
        self.pop_size = pop_size
        self.population = []
        self.letters = string.ascii_lowercase + ' '
        self.id = id
        self.goal = goal

    def mutate(self, parent, characters=1) -> str:
        """Generates a mutation from parent"""
        mutation = list(parent.content)
        previous_indexes = []
        for _ in range(characters):
            index = random.randint(0, len(parent.content) - 1)
            while index in previous_indexes:
                index = random.randint(0, len(parent.content) - 1)
            previous_indexes.append(index)
            mutation[index] = random.choice(self.letters)
        content = "".join(mutation)
        return String(content, self.goal)

    def generate_pop(self) -> List:
        for _ in range(self.pop_size):
            self.population.append(self.mutate(self.parent))
        return self.population

    def fittest(self) -> String:
        if self.population:
            best = self.population[0]
            for obj in self.population:
                if obj.score > best.score:
                    best = obj
        return best

