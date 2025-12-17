#List of questions
#Store the answer
#Random picked questions
#Point system
#Limitation of mistakes for each questions that resets after you get one right
import random

questions = {
    "What is the first letter in the alphabet": "A",
    "What is the last letter in the alphabet": "Z",
    "What is the lowest number": "0",
    "Give an example of a prime number": "1",
    "How many fingers does a human body have": "10",
    "What is the 3rd letter in the alphabet": "C"
}

def random_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0
    mistake = 0
    
    selected_questions = random.sample(questions_list, total_questions)
    
    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip()
        
        correct_answer = questions[question]
        
        if user_answer == correct_answer.lower():
            print("Correct! \n")
            score += 1
            mistake = 0
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}. \n")
            mistake += 1
            
        if mistake == 3:
            print("You ran out of lives, please try again.")
            quit()
        
    print(f"The score you got is: {score}/{total_questions}")
    
random_trivia_game()