import random

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

        if guess in self.word.lower():
            print(f"Good guess! '{guess}' is in the word.")

            for i, letter in enumerate(self.word):
                if letter.lower() == guess:
                    self.word_guessed[i] = letter 
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)  
                break

def play_game(word_list):
    num_lives = 10
    game = Hangman(word_list, num_lives)

    while True:
        print("Word Guessed:", ''.join(game.word_guessed))
        print("Remaining Unique Letters:", game.num_letters)
        game.ask_for_input()

        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters == 0 or ''.join(game.word_guessed) == game.word:
            print("Congratulations. You won the game!")
            break


if __name__ == "__main__":
    words_to_guess = ["Strawberry", "Cherry", "Pineapple", "Mango", "Orange"]  
    play_game(words_to_guess)
