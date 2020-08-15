"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!


def main():
    # calculate result based on score
    score = float(input("Enter score: "))
    result = calculate_score(score)
    print(result)


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