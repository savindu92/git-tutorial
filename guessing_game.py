#! /usr/bin/python3

import random

def guess_loop():
    print("What is your name")
    name = input()
    en_combien_essaies = 0
    number_to_guess = random.randint(1, 100)
    print("I have in mind a number in between 1 and 100, can you find it?")
    while True:
        try:
            guess = int(input())
            if guess > number_to_guess:
                print("The number to guess is lower")
                en_combien_essaies = en_combien_essaies + 1
            elif guess < number_to_guess:
                print("The number to guess is higher")
                en_combien_essaies = en_combien_essaies + 1
            else:
                print(name, "just found the number with",		 en_combien_essaies,  "tries it was indeed",guess)
                return
        except ValueError as err:
            print("Invalid input , please enter an integer")

guess_loop()
