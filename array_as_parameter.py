#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Dec 2019
# This program uses a list as a parameter

import random


def sum_of_numbers(list_of_numbers):
    # this functions add up all the numbers in the list

    total = 0

    for counter in range(0, len(list_of_numbers)):
        total += list_of_numbers[counter]

    return total


def main():
    # this function uses a list

    random_numbers = []
    sum = 0

    # input
    print("The numbers are ")
    for loop_counter in range(0, 9):
        a_single_number = random.randint(0, 10)
        random_numbers.append(a_single_number)
        print("{0}, ".format(a_single_number), end="")
    print("")

    sum = sum_of_numbers(random_numbers)

    print("The sum of all the numbers is: {0} ".format(sum))
    print("The biggest of all the numbers is: {0} ".format
          (max(random_numbers)))


if __name__ == "__main__":
    main()
