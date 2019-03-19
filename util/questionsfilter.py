class QuestionsFilter:
    @staticmethod
    def filter_questions_with_target_marks(questions_list, target_marks):
        curr_sum, start = questions_list[0].get_marks(), 0
        for idx in range(1, len(questions_list) + 1):
            while curr_sum > target_marks and start < idx - 1:
                curr_sum = curr_sum - questions_list[start].get_marks()
                start = start + 1

            if curr_sum == target_marks:
                return questions_list[start:idx - 1]

            if idx < len(questions_list):
                curr_sum = curr_sum + questions_list[idx].get_marks()

        return None
