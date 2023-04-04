'''
this is the code for an easy quiz game.
here we import question class from question.py
'''

from question import question


# these are some of the easy questions build for the quiz
question_prompts = [
    "what color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "what color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "what color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]
    
  
# here we assign the answers for the questions build  
questions = [
    question(question_prompts[0], "a"),  
    question(question_prompts[1], "c"), 
    question(question_prompts[2], "b"), 
]


# this is the main function where we check the entered answer is correct is not.
def run_test(questions):
    
    # initially assign the score as 0
    score = 0
    
    # create a for loop to check the answers question by question and to increment the score
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + " correct")
    
run_test(questions)
