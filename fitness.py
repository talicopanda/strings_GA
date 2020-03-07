"""Fitness model"""
import string

class fitness:
    scoreForRightPlace: int
    scoreForRightLetter: int
    goal: str

    def __init__(self, goal: str):
        self.scoreForRightPlace = 3
        self.scoreForRightLetter = 1
        self.goal = goal


    def judge(self, word: string):
        word.setScore((self.scoreForRightPlace(word.content) +
                       self.scoreForRightLetter(word.content))
                      /(self.scoreForRightLetter*len(word.content)
                        + self.scoreForRightPlace*len(word.content)))



    def scoreForRightPlace(self, word: str) -> int:
        for i in range(len(word)):
            if self.goal


    def scoreForRightLetters(self, word: str) ->int:
