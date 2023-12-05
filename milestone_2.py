import random
'''Created word list with favourite fruits. '''

word_list = ["Strawberry", "Cherry", "Pineapple", "Mango", "Orange"]
print(word_list)

''' Created random generator '''
word = random.choice(word_list)

print(word)

''' Taking input from user '''

guess = input("Please enter a single letter:")

''' Checking only one alphabetical character is entered. Using if else statement to check for this condition.'''

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")







