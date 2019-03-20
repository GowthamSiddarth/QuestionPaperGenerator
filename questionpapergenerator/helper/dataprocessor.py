class DataProcessor:
    @staticmethod
    def group_by_difficulty_with_questions_sorted(questions_list):
        questions_group = {}
        for question in questions_list:
            questions_group[question.get_difficulty()] = questions_group.get(question.get_difficulty(), []) + [question]

        for difficulty_group, questions_from_group in questions_group.items():
            questions_group[difficulty_group] = sorted(questions_from_group, key=lambda question: (
                question.get_marks(), question.get_question_number()))

        return questions_group
