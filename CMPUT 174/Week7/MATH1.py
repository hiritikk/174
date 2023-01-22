'''
v1- display the header
v2 - ask_a_question
v3 - ask_questions
v4 - run_quiz
v5 - run_quiz multiple times
v6 - number of quizzes, highest score, quizzes that have highest score
'''

def display_header(string:str)->None:
    "dispays the header"
    print(f'+{len(string) * "-"}+')
    print(f'{string}|')
    print(f'+{len(string) * "-"}+')
    
def main():
    display_header('Math is fun - Start')
main()
    