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
        pass
        #for i in range(len(word)):
        #    if self.goal

    def scoreForRightLetters(self, word: str) -> int:
        error_for_each_letter = {}


        for char in self.goal:
            error_for_each_letter[char] = abs(self.goal.count(char) - word.count(char))

        total_error = 0
        for key in error_for_each_letter:
            total_error += error_for_each_letter[key]


        return max((len(self.goal) * self.scoreForRightLetter) - total_error, 0)




