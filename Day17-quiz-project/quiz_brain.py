class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        result = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {result.text} (True/False): ").lower()
        self.check_answer(answer, result.answer)

    def has_next_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("Correct!")
        else:
            print("Wrong!")
        print(f"Score: {self.score}/{self.question_number}")
        print("\n")
