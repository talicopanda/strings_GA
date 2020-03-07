import random
import string


class Population:
    """Creates a population based on mutation of a single element
    """

    def __init__(self, parent: str):
        self.parent = parent


    def generate_string(length: int) -> str:
        """Generates a random string of 'abcdefghijklmnopqrstuvwxyz ' with
        length <length>."""
        letters = string.ascii_lowercase + ' '
        return ''.join(random.choice(letters) for i in range(length))


if __name__ == '__main__':
    pop = Population()
    for i in range(50):
        print(generate_string(i))
