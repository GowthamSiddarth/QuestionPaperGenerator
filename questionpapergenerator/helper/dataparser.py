from questionpapergenerator.models.difficulty import DifficultyLevel
from questionpapergenerator.models.question import Question


class DataParser:
    def __init__(self, data_set_path):
        self._data_set_path = data_set_path
        self._num_of_questions, self._questions, self._total_marks, self._marks_distribution = DataParser._read_input(
            self)

    def get_num_of_questions(self):
        return self._num_of_questions

    def get_questions(self):
        return self._questions

    def get_total_marks(self):
        return self._total_marks

    def get_marks_distribution(self):
        return self._marks_distribution

    @staticmethod
    def _map_meta_data_to_question_paper(meta_data):
        cols = meta_data.split(', ')
        return Question(int(cols[0][1:]), cols[1], int(cols[2]))

    @staticmethod
    def _read_input(self):
        with open(self._data_set_path) as data_set_file:
            content = data_set_file.readlines()

        content = [line.strip() for line in content]
        num_of_questions = int(content[0])
        questions = [self._map_meta_data_to_question_paper(line) for line in content[1:-1]]
        last_line_cols = content[-1].split(', ')
        total_marks = int(last_line_cols[0])
        marks_distribution = {}
        for idx in range(1, len(last_line_cols)):
            cols = last_line_cols[idx].split(' ')
            marks_distribution[DifficultyLevel[cols[0]]] = (int(cols[1]) * total_marks) / 100

        return num_of_questions, questions, total_marks, marks_distribution
