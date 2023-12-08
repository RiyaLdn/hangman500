import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self._get_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

        print(f"The mystery word has {len(self.word)} characters")
        print(" ".join(self.word_guessed))

    def _get_random_word(self):
        return random.choice(self.word_list)

    def check_letter(self, guess):
        guess = guess.lower()

        if guess in self.word.lower():
            print(f"Good guess! '{guess}' is in the word.")

            for i, letter in enumerate(self.word):
                if letter.lower() == guess:
                    self.word_guessed[i] = letter.upper()  
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            
        print(" ".join(self.word_guessed))  
        

    def ask_letter(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print(" Please enter just one character.")
            elif guess in self.list_of_guesses:
                print(f" '{guess}' was already tried!")
            else:
                self.check_letter(guess)
                self.list_of_guesses.append(guess)  
                break

def play_game(word_list, num_lives=5):
    game = Hangman(word_list, num_lives)

    while True:
        game.ask_letter()  

        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}.")
            break
        elif game.num_letters == 0 or ''.join(game.word_guessed) == game.word:
            print("Congratulations. You won!")
            break

if __name__ == "__main__":
    word_list = ["Strawberry", "Cherry", "Pineapple", "Mango", "Orange"]  
    play_game(word_list)
