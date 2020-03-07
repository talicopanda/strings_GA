import random
from typing import List
import string
import doctest

class String:
    """Creates a String object"""
    content: str
    score: float
    goal: str

    def __init__(self, content: str):
        self.correct_place_score = 3
        self.right_letter_score = 1
        self.goal = "poop"
        self.content = content
        self.score = calc_score(content, self.goal)

    def __str__(self) -> str:
        return f'self.content ({self.score})'

    def judge(self, word: string):
        word.setScore((self.correct_place_score(word.content) +
                       self.right_letter_score(word.content))
                      / (self.right_letter_score * len(word.content)
                         + self.correct_place_score * len(word.content)))

    def score_for_right_place(self, word: str, goal: str) -> int:
        """
        >>> ftns = String("Po p ")
        >>> ftns.score
        12
        >>> ftns = String("     ")
        >>> ftns.score
        6
        """
        score = 0
        for i in range(len(word)):
            if goal[i] == word[i]:
                score += self.correct_place_score
        return score

    def right_letters_score(self, word: str, goal: str) -> int:
        error_for_each_letter = {}
        for char in goal:
            error_for_each_letter[char] = abs(goal.count(char) - word.count(char))
        total_error = 0
        for key in error_for_each_letter:
            total_error += error_for_each_letter[key]
        return max((len(goal) * self.right_letter_score) - total_error, 0)

    def calc_score(self, content: str, goal: str):
        pass

if __name__ == "__main__":
    doctest.testmod()


