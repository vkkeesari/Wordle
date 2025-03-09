# Vidhu Keesari
# 1/6/23
# 7625469239


'''
This program replicates the game wordle
'''
'''
One thing that surprised me is how well my code works and how 
efficient is it. One challenge i had during this project was figuring
out how to use a specific library. No one helped me during this 
project. Satisfied. I chose this because I know I did a good job and 
it didn't even talk me that long. If I had more time on this project 
i would add a interface so its easier to play.

'''

import requests
import random


def get_password():
    '''
    The function below asks for the password so the user can access the
    program. If the user enters the wrong password, it asks them to enter it
    again
    '''
    while True:
        passwrd = input("Enter password: ")
        if passwrd == "password":
            break
        else:
            print("Incorrect password try again")


def get_word():
    '''
    The function below goes to a website, reads the text, and splits it into
    a list. Then we use the random import and we randomize a index, use the
    randomized index in the big list of words and check if the word is a 5
    letter word. If it is, we continue with the program, and if it isn't it
    randomized the input again and keeps checking for a 5 ltter word.
    '''
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    words = response.content.splitlines()

    while True:
        index = random.randrange(0, 10001)
        word_to_get = words[index]
        if len(word_to_get) == word_length:
            break
    word_to_guess = str(word_to_get, 'UTF-8')
    return (word_to_guess)


def guess_word(word_to_guess, word_length, num_guesses):
    '''
    The function below starts with checking the difficulty the user
    wanted. It makes sure the input is the right amount of letters in
    the word. Then it checks if the word is the word guessed.
    After this it goes into a for loop chekcing if the each letter is in
    the word. If it is in the word, then it checks if it is in the same
    index. If it is, it append G to the list, and if it isn't, it
    appends Y to the list. If the letter is not even in the word, it
    appends R to the list. The program then prints the output list after
    every guess and prints how many more tries you have to guess the word.
    If you didn't guess the word with how many guesses you chose, then it
    prints that you didn't guess the word and it tell you the word.
    '''
    # print(word_to_guess)
    ctr = 0
    if num_guesses == "b":
        num_guesses = 6
    elif num_guesses == 'i':
        num_guesses = 5
    elif num_guesses == 'e':
        num_guesses = 4
    while ctr != num_guesses:
        output = []
        user_guess = input("Enter your guess: ")
        user_guess = user_guess.lower()
        if len(user_guess) != word_length:
            print("Has to be a", word_length, "letter word!")
            continue
        if user_guess == str(word_to_guess):
            print("Congratulations! You figured out the word. It was ", str(word_to_guess))
            exit()
        for i in range(word_length):
            if user_guess[i] in str(word_to_guess):
                if user_guess[i] == str(word_to_guess[i]):
                    output.append("G")
                    continue
                output.append("Y")
                continue
            output.append("R")
        print(list(user_guess))
        print(output)

        print("you only have ", num_guesses - (ctr + 1), " guesses left")
        ctr += 1
    print("You did not guess the word with your", num_guesses, "guesses. The word was ", str(word_to_guess))


'''
The program starts with checking for the password. Then it asks for 
how many letters word they want to guess. Then it asks for the 
difficulty.

'''

# prints finals
print("The Password is password")
print()
print()
print()

get_password()
print()
print()
# prints basic info
print("Welcome to Wordle")
print("G = In word and in right spot")
print("Y = In word but in wrong spot")
print("R = Not in word")
print()
print()
print()
print("Word length has to be in between 3-6")
# This while loop asks the user for how mnay letter they want in the word
while True:
    try:
        word_length = int(input("How many letter word do you want to guess: "))
    except ValueError:
        print("Has to be a number")
        continue
    if word_length > 6 or word_length < 3:
        print("Word length has to be in between 3-6")
        continue
    break
print()
print()
print()
# Prints difficulty
print("Begginer = 6 guesses")
print("Intermediate = 5 guesses")
print("Expert = 4 guesses")
# Asks for for difficulty
while True:
    num_guesses = input("Begginer, intermediate, expert(B, I, E): ")
    num_guesses = num_guesses.lower()
    if num_guesses == 'b' or num_guesses == 'i' or num_guesses == 'e' and len(num_guesses) == 1:
        break
    print("Has to be b, i or e")
guess_word(get_word(), word_length, num_guesses)























