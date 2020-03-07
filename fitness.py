"""Fitness model"""
import string
import doctest

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
        """

        :param word:
        :return:
        >>> ftns = fitness("Hello hi")
        >>> ftns.scoreForRightPlace("hello hi")
        24
        """
        score = 0
        for i in range(len(word)):
            if self.goal[i] == word[i]:
                score += self.scoreForRightPlace



    def scoreForRightLetters(self, word: str) ->int:
        pass


if __name__ == "main":

