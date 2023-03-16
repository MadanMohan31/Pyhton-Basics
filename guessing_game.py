# code for a game of guessing words.
# this code will have 3 limits to guess the word.


secret_word = "lion"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter guess : ")
        guess_count += 1
    else:
        out_of_guesses = True
    
if out_of_guesses:
    print("Out of guesses, YOU LOSE!!")
else:
    print("YOU WIN!!")
