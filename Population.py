import random
from typing import List
import string

import String


class Population:
    """Creates a population based on mutation of a single element
    """
    parent: String
    pop_size: int
    population: List
    letters: str
    id: int

    def __init__(self, parent: String, pop_size: int, id: int):
        self.parent = parent
        self.pop_size = pop_size
        self.population = []
        self.letters = string.ascii_lowercase + ' '
        self.id = id

    def mutate(self, parent, characters=1) -> str:
        """Generates a mutation from parent"""
        mutation = list(parent.content)
        previous_indexes = []
        for _ in range(characters):
            index = random.randint(0, len(parent) - 1)
            while index in previous_indexes:
                index = random.randint(0, len(parent) - 1)
            previous_indexes.append(index)
            mutation[index] = random.choice(self.letters)
        content = "".join(mutation)
        return String(content)

    def generate_pop(self) -> List[String]:
        for _ in range(self.pop_size):
            self.population.append(self.mutate(self.parent))
        return self.population

    def fittest(self):
        


if __name__ == '__main__':
    tales = Population('tales', 50)
    pop = tales.generate_pop()
    print(pop)
