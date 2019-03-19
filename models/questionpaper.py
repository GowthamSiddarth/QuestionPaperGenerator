from models.difficulty import DifficultyLevel


class QuestionPaper:
    def __init__(self, question_number, difficulty, marks):
        self.question_number = question_number
        self.difficulty = DifficultyLevel[difficulty]
        self.marks = marks
