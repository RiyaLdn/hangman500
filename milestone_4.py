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

'''Creates class called Hangman'''

class Hangman:
    def __init__(self, word_list, num_lives=10):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self._get_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def _get_random_word(self):
        return random.choice(self.word_list)

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")

            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess  
                    self.num_letters -= 1 
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")
                    
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter just one character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)  
                break

hangman_game = Hangman(word_list=["Strawberry", "Cherry", "Pineapple", "Mango", "Orange"])
hangman_game.check_guess('e')  
print("Word Guessed:", ''.join(hangman_game.word_guessed))
print("Remaining Unique Letters:", hangman_game.num_letters)
''''''
