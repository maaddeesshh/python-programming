# Define a Question class
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# List of question prompts
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n"
]

# Create a list of Question objects
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

# Function to run the quiz
def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            score += 1
    print("You got " + str(score) + " out of " + str(len(questions)) + " correct.")


# Start the quiz
run_quiz(questions)
