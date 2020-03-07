"""Fitness model"""
import string
import doctest


class fitness:
    ScoreForRightPlace: int
    ScoreForRightLetter: int
    goal: str

    def __init__(self, goal: str):
        self.scoreForRightPlace = 3
        self.scoreForRightLetter = 1
        self.goal = goal

    def judge(self, word: string):
        word.setScore((self.scoreForRightPlace(word.content) +
                       self.scoreForRightLetter(word.content))
                      / (self.scoreForRightLetter * len(word.content)
                         + self.scoreForRightPlace * len(word.content)))

    def score_for_right_place(self, word: str) -> int:
        """

        :param word:
        :return:
        >>> ftns = fitness("Hello hi")
        >>> ftns.score_for_right_place("hello hi")
        21
        >>> ftns = fitness("    ")
        >>> ftns.score_for_right_place("    ")
        12
        >>> ftns = fitness(" H h")
        >>> ftns.score_for_right_place("    ")
        6
        """
        score = 0
        for i in range(len(word)):
            if self.goal[i] == word[i]:
                score += self.scoreForRightPlace
        return score

    def scoreForRightLetters(self, word: str) -> int:
        pass


if __name__ == "__main__":

    doctest.testmod()
