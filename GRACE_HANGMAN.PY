import random
from WORDS import word_list
def welcome():
    print("Welcome to Hangman Game.")
    name=input("Enter your Name:-").capitalize()
    if name.isalpha()==True:
        print("Hi!",name,"glad to have you here.")
        print("You will be playing against the computer.")
        print("Good Luck! Have fun playing.")
    else:
        print("Please enter your name using letter only.")
        name=input("Enter your name here:-").capitalize()
        print("Hi!",name,"Good Luck! Have fun playing.")
def play_again():
    print("Would you like to play again?Yes/No")
    choice=input("Enter y or n:-").lower()
    if choice=="y":
        game_run()
    else:
        print("Hope you had fun playing the game. See you next time")
def game_run():
    welcome()
    stages = ['''
        +---+
        |   |
            |
            |
            |
            |
            =========''', '''
        +---+
        |   |
        0   |
            |
            |
            |
            =========''', '''
        +---+
        |   |
        0   |
       /    |
            |
            |
            =========''', '''
        +---+
        |   |
        0   |
       /|   |
            |
            |
            =========''', '''
        +---+
        |   |
        0   |
       /|\  |
            |
            |
            =========''', '''
        +---+
        |   |
        0   |
       /|\  |
        |   |
            |
            =========''', '''
        +---+
        |   |
        0   |
       /|\  |
        |   |
       /    |
            =========''', '''
        +---+
        |   |
        0   |
       /|\  |
        |   |
       / \  |
            ========='''
    ]
    word=random.choice(word_list).lower()
    guessed_correctly=[]
    guessed_incorrectly=[]
    stages_count=0
    tries=7
    print("The word contains",len(word),"letters.")
    while tries>0:
        word_completion=""
        for letter in word:
            if letter in guessed_correctly:
                word_completion+= letter
            else:
                word_completion+= "_"
        if  word_completion==word:
            print(word_completion.capitalize())
            print("Congrats!! You guess the word correctly!You win")
            break
        print("Guess the word",word_completion)
        print("You have",tries,"chances left")
        guess=input("Guess a letter in  the word  or enter the full word:-").lower()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_correctly:
                print("you have already guess the letter before.")
            elif guess not in word:
                print("Sorry! that letter is not in the word.")
                stages_count = stages_count+1
                tries = tries-1
                guessed_incorrectly.append(guess)
                print(stages[stages_count])
            elif guess in word:
                print("Good job",guess,"is in the word!")
                guessed_correctly.append(guess)
        elif len(guess)==len(word):
            if guess in guessed_incorrectly:
                    print("You already guessed the word",guess)
            elif guess!=word:
                print(guess,"is not in the word.")
                stages_count = stages_count +1
                tries = tries-1
                guessed_incorrectly.append(guess)
                print(stages[stages_count])
        else:
            print("The length of your guess is not the same as the length of the correct word.")
            stages_count = stages_count +1
            tries = tries-1
            guessed_incorrectly.append(guess)
            print(stages[stages_count])
    if tries==0:
        print("Sorry!.You ran out of tries.The word was",word.capitalize(),"maybe next time.")
    play_again()
game_run()