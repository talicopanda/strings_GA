import random
import string

class Population:
    """Creates a population based on mutation of a single element
    """

    def __init__(self, parent: str):
        self.parent = parent


    def generate_string(length: int) -> str:
        """Generates a random string of 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM
        NOPQRSTUVWXYZ ' with length <length>."""
        letters = string.ascii_letters + ' '
        return ''.join(random.choice(letters) for i in range(stringLength))
