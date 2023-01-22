'''
v1- display the header
v2 - ask_a_question
v3 - ask_questions
v4 - run_quiz
v5 - run_quiz multiple times
v6 - number of quizzes, highest score, quizzes that have highest score
'''
import random 

def display_header(string:str)->None:
    "dispays the header"
    print(f'+{len(string) * "-"}+')
    print(f'{string}|')
    print(f'+{len(string) * "-"}+')
    
def ask_a_question()->bool:
    operators = ("+","-","*")
    op = random.choice(operators)
    X = random.randint(1,10)
    y = random.randint(1,10)
    question = f'{x} {op} {y} = '
    answer = int(input(question))
    if op =='+':
        correct_anwser = x + y
    elif op == "-":
        correct_anwser = x - y
    elif op == "*":
        correct_anwser = x * y
    return correct_anwser


def ask_question()->int:
    quiz_score = 0 
    
    for index in range(3):
        result = ask_a_question()
        if result:
            print('correct')
            quiz_score += 1
        else:
            print('Incorrect')
    print(f'Quiz score {quiz_score}/3')
    return quiz_score



    
def main():
    display_header('Math is fun - Start')
    print(ask_question())                 #how does this run with out calling it 


main()