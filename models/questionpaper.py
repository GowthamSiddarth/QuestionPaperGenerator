from models.difficulty import DifficultyLevel


class QuestionPaper:
    def __init__(self, question_number, difficulty, marks):
        self._question_number = question_number
        self._difficulty = DifficultyLevel[difficulty]
        self._marks = marks

    def get_question_number(self):
        return self._question_number

    def get_difficulty(self):
        return self._difficulty

    def get_marks(self):
        return self._marks
