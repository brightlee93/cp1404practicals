"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

# do from scratch exercises Q1 b
# def main():
#     # calculate result based on score
#     score = float(input("Enter score: "))
#     result = calculate_score(score)
#     print(result)
#
#
# def calculate_score(score):
#     # sort score into result category
#     if score < 0 or score > 100:
#         result = "Invalid score"
#     elif score >= 90:
#         result = "Excellent"
#     elif score >= 50:
#         result = "Passable"
#     else:
#         result = "Bad"
#     return result
#
#
# main()


# do from scratch exercises Q1 c

import random


def main():
    # calculate result based on random score
    score = random.randint(0,100)
    result = calculate_score(score)
    print("A score of {0} is {1}".format(score,result))


def calculate_score(score):
    # sort score into result category
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()