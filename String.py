"""Creates a string object"""

class String:

    content: str
    score: float

    def __init__(self, content: str):
        self.content = content

    def setScore(self, score: float):
        self.score = score

