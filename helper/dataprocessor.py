from models.questionpaper import QuestionPaper
from models.difficulty import DifficultyLevel


class DataProcessor:
    def __init__(self, data_set_path):
        self.data_set_path = data_set_path

    def read_input(self):
        with open(self.data_set_path) as data_set_file:
            content = data_set_file.readlines()

        content = [line.strip() for line in content]
        self.num_of_questions = int(content[0])
        self.questions = [QuestionPaper(cols[0][1], cols[1], cols[2]) for line in content[1:-1] for cols in
                          line.split(', ')]
