import random
from typing import List
import string


class Population:
    """Creates a population based on mutation of a single element
    """

    def __init__(self, parent: str, pop_size: int):
        self.parent = parent
        self.pop_size = pop_size
        self.population = []
        self.letters = string.ascii_lowercase + ' '

    def first_string(self, size: int) -> str:
        """Generates a random string of 'abcdefghijklmnopqrstuvwxyz '."""
        return ''.join(random.choice(self.letters) for _ in range(size))

    def mutate_string(self, parent, characters = 1) -> str:
        """Generates a mutation from parent"""
        mutation = list(parent)
        previous_indexes = []
        for _ in range(characters):
            index = random.randint(0, len(parent) - 1)
            while index in previous_indexes:
                index = random.randint(0, len(parent) - 1)
            previous_indexes.append(index)
            mutation[index] = random.choice(self.letters)
        return "".join(mutation)

    def generate_pop(self) -> List[str]: #List[String]
        for _ in range(self.pop_size):
            self.population.append(self.mutate_string(self.parent))
        return self.population




if __name__ == '__main__':
    tales = Population('tales', 50)
    pop = tales.generate_pop()
    print(pop)
