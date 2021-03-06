import random
from typing import List
import string
import doctest


class String:
    """Creates a String object"""
    content: str
    score: float
    goal: str

    def __init__(self, content: str, goal: str):
        self.correct_place_score = 3
        self.right_letter_score = 1
        self.goal = goal
        self.content = content
        self.score = self.calc_score()

    def __str__(self) -> str:
        return f'{self.content} ({self.score})'

    def judge(self, word: string):
        word.setScore((self.correct_place_score(word.content) +
                       self.right_letter_score(word.content))
                      / (self.right_letter_score * len(word.content)
                         + self.correct_place_score * len(word.content)))

    def score_for_right_place(self, word: str) -> int:
        """
        >>> ftns = String("Po p ")
        >>> print(ftns.score)
        12
        >>> ftns = String("     ")
        >>> print(ftns.score)
        6
        """
        score = 0
        for i in range(len(word)):
            if self.goal[i] == word[i]:
                score += self.correct_place_score
        return score

    def right_letters_score(self) -> int:
        """
        >>> s = String('pope')
        >>> s.right_letter_score()
        2
        >>> s2 = String('lmrt')
        >>> s2.right_letter_score()
        0
        >>> s3 = String('ptuv')
        >>> s3.right_letter_score()
        1
        """
        error_for_each_letter = {}
        for char in self.goal:
            error_for_each_letter[char] = abs(
                self.goal.count(char) - self.content.count(char))
        total_error = 0
        for key in error_for_each_letter:
            total_error += error_for_each_letter[key]
        return max((len(self.goal) * self.right_letter_score) - total_error, 0)

    def calc_score(self):
        size = len(self.content)
        return (self.score_for_right_place(self.content) +
                self.right_letters_score()) / \
               (
                           size * self.correct_place_score + size * self.right_letter_score)
