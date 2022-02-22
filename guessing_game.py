secret_word = "giraffe" #harcoded secret word
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
        print("Out of guesses, you lose!")
        exit()
    
print("You win!")