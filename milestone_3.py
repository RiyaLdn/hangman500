import random
'''Created word list with favourite fruits. '''

word_list = ["Strawberry", "Cherry", "Pineapple", "Mango", "Orange"]
print(word_list)

''' Created random generator '''
word = random.choice(word_list)

print(word)

''' Creates function to check the guess'''
def check_guess(guess, word):
    guess = guess.lower()

    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word.")

''' Creates function to ask for user input'''
def ask_for_input():
    while True:
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            check_guess(guess, word)  

            break
        else:
            print("Invalid input. Please enter a single letter.")

ask_for_input()


