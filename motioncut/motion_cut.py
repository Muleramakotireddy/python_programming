def ask_question(question_data, question_number):
    question = question_data["question"]
    options = question_data["options"]
    correct_answer = question_data["correct_answer"]
    feedback = question_data["feedback"]
    print(f"\nQuestion {question_number}: {question}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= len(options):
                break
            else:
                print(f"Please enter a number between 1 and {len(options)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer was: {options[correct_answer - 1]}")
    print(f"Feedback: {feedback}")
    return answer == correct_answer
def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Madrid"],
            "correct_answer": 1,
            "feedback": "Paris is the capital and most populous city of France."
        },
        {
            "question": "What is the correct file extension for Python files?",
            "options": [".pt", ".pyth", ".pyt", ".py"],
            "correct_answer": 4,
            "feedback": "In Python, the correct file extension for scripts is \".py\". This extension tells the operating system and text editors that the file contains Python code."
        },
        {
            "question": "What is the correct syntax to output the type of a variable or object in Python?",
            "options": ["print(type(x))", "print(typeof(x))", "print(typeof x)", "print(typeOf(x))"],
            "correct_answer": 1,
            "feedback": "In Python, to output the type of a variable or object, you use the \"type()\" function, and the correct syntax is: print(type(x))"
        },
        {
            "question": "Which of these collections defines a LIST?",
            "options": [
                "{\"name\": \"apple\", \"color\": \"green\"}",
                "(\"apple\", \"banana\", \"cherry\")",
                "{\"apple\", \"banana\", \"cherry\"}",
                "[\"apple\", \"banana\", \"cherry\"]"
            ],
            "correct_answer": 4,
            "feedback": "In Python, a list is defined using square brackets [], and it is an ordered collection that allows duplicate elements and can be modified. The correct list syntax is: [\"apple\", \"banana\", \"cherry\"]"
        }
    ]
    score = 0
    for i, question_data in enumerate(questions, 1):
        if ask_question(question_data, i):
            score += 1
    print(f"\nYour final score is {score} out of {len(questions)}")
if __name__ == "__main__":
    run_quiz()
