from helper.dataparser import DataParser
from helper.dataprocessor import DataProcessor
from util.questionsfilter import QuestionsFilter
import itertools

if __name__ == '__main__':
    data_set_path = 'data/sample-input.txt'
    data_parser = DataParser(data_set_path=data_set_path)
    questions_group = data_parser.get_questions()

    data_processor = DataProcessor()
    sorted_questions_group = data_processor.group_by_difficulty_with_questions_sorted(questions_group)

    marks_distribution = data_parser.get_marks_distribution()
    question_paper = list(itertools.chain(*[
        QuestionsFilter.filter_questions_with_target_marks(sorted_questions_group[difficulty_group], target_marks) for
        difficulty_group, target_marks in marks_distribution.items()]))

    for question in question_paper:
        print(question)
