#!/usr/bin/env python3
# Created By: Emmanuella Taiwo
# created on 16th Nov, 2026
# This program asks the for a number between 0 and 9 and
# checks if the input is valid or not. If the input is valid,
# it will display the number back to the user in a loop and break.
import random


def main():
    # a number between 0 and 9
    random_variable = random.randint(0, 9)

    while True:
        # get the number from the user and convert to an integer
        try:
            number = int(input("Enter a number between 0 and 9: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return

        # check if the number is correct and display the result
        if number == random_variable:
            print("You are correct: {0}".format(number))
            break
        else:
            print("You are wrong. Try again.")


if __name__ == "__main__":
    main()
