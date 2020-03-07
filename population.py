import random
import string


class Population:
    """Creates a population based on mutation of a single element
    """

    def __init__(self, parent: str, pop_size: int):
        self.parent = parent
        self.parent_len = len(parent)
        self.pop_size = pop_size

    def generate_pop(self):


    def first_string(self) -> str:
        """Generates a random string of 'abcdefghijklmnopqrstuvwxyz '."""
        letters = string.ascii_lowercase + ' '
        return ''.join(random.choice(letters) for _ in range(self.parent_len))

    def mutate_string(self, characters = 1) -> str:
        """Generates a mutation from parent"""
        letters = string.ascii_lowercase + ' '
        mutation = self.parent
        previous_indexes = []
        for _ in range(characters):
            index = random.randint(0, self.string_len - 1)
            while index in previous_indexes:
                index = random.randint(0, self.string_len - 1)
            previous_indexes.append(index)
            mutation[index] = random.choice(letters)
        return mutation




if __name__ == '__main__':
    pop = Population()
    for i in range(50):
        print(generate_string(i))
