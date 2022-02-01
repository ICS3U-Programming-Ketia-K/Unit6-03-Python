#!/usr/bin/env python3
# Created by: Ketia Gaelle Kaze
# Created on: Jan. 29, 2022
# This program uses a for loop to generate
# 10 random numbers in a list, then
# displays the smallest value
import constants
import random


# This function calculates the max value in the list
def find_min_value(random_numbers):

    min_value = random_numbers[0]

    # calculate the min value
    for loop_counter in random_numbers:
        if min_value > loop_counter:
            min_value = loop_counter

    return min_value


def main():
    # initializing counter
    loop_counter = 0
    # declaring variable
    random_numbers_user = []
    # display opening message to console
    print("This program generates a list of 10 random "
          "numbers between 0 and 100, then determines the smallest number.")
    print("")

    # display random numbers and minimum value
    for loop_counter in range(constants.MAX_ARRAY_SIZE):
        random_numbers_user.append(random.randint(constants.MIN_NUM,
                                                  constants.MAX_NUM))
        print("{} added to the list at "
              "position {}"
              .format(random_numbers_user[loop_counter], loop_counter))

    min_user = find_min_value(random_numbers_user)
    print("")
    print("The minimum value is: {}" .format(min_user))


if __name__ == "__main__":
    main()
