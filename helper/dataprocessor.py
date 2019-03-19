from models.questionpaper import QuestionPaper
from models.difficulty import DifficultyLevel


class DataProcessor:
    def __init__(self, data_set_path):
        self._data_set_path = data_set_path
        self._num_of_questions, self._questions, self._total_marks, self.marks_distribution = DataProcessor.read_input()

    @staticmethod
    def _map_meta_data_to_question_paper(meta_data):
        cols = meta_data.split(', ')
        return QuestionPaper(cols[0][1], cols[1], cols[2])

    @staticmethod
    def read_input(self):
        with open(self._data_set_path) as data_set_file:
            content = data_set_file.readlines()

        content = [line.strip() for line in content]
        num_of_questions = int(content[0])
        for line in content[1:-1]:
            print(line.split(', '))
        questions = [self._map_meta_data_to_question_paper(line) for line in content[1:-1]]
        last_line_cols = content[-1].split(', ')
        total_marks = int(last_line_cols[0])
        marks_distribution = {}
        for idx in range(1, len(last_line_cols)):
            cols = last_line_cols[idx].split(' ')
            marks_distribution[DifficultyLevel[cols[0]]] = int(cols[1])

        return num_of_questions, questions, total_marks, marks_distribution
