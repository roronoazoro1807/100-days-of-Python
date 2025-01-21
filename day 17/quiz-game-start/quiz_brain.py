class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        # Check if the current question index is less than the total number of questions
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Get the current question
        current_question = self.question_list[self.question_number]
        # Increment the question number
        self.question_number += 1
        # Ask the user for their answer
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # Check if the answer is correct
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        # Compare the user's answer with the correct answer (case-insensitive)
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}\n")
        # Print the current score
        print(f"Your current score is: {self.score}/{self.question_number}\n")
