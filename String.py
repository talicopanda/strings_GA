import random
from typing import List
import string

class String:
    """Creates a String object"""
    content: str
    score: float

    def __init__(self, content: str):
        self.content = content
        self.score = calc_score(content)

    def __str__(self) -> str:
        return f'self.content ({self.score})'

    def calc_score(self, score: float):
        self.score = score

