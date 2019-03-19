from helper.dataparser import DataParser
from helper.dataprocessor import DataProcessor

if __name__ == '__main__':
    data_set_path = 'data/sample-input.txt'
    data_parser = DataParser(data_set_path=data_set_path)
    questions_group = data_parser.get_questions()

    data_processor = DataProcessor()
    sorted_questions_group = data_processor.group_by_difficulty_with_questions_sorted(questions_group)
