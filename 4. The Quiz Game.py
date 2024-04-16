# Objective:
# The aim of this assignment is to create a quiz game that asks questions and checks answers.

# Task 1: Develop a list of questions and answers.
# Task 2: Write a function that quizzes the user and takes their answers.
# Task 3: Score the quiz and give the user feedback on their performance.

questions = [
    {
        "question": "What is 2+2?",
        "answer": "4"
    },
    {
        "question": "What color is a firetruck?",
        "answer": "red"
    },
    {
        "question": "What year is it?",
        "answer": "2024"
    },
    {
        "question": "What country has the highest population?",
        "answer": "India"
    },
    {
        "question": "What is the tallest building in the world?",
        "answer": "Burj Khalifa"
    },
]

correct_answers=0
for question_object in questions:
    question=question_object["question"]
    answer=question_object["answer"]
    user_answer = input(question)
    if user_answer.lower() == answer.lower():
        correct_answers+=1
    
print(f"You answered {correct_answers} out of {len(questions)} questions correctly")