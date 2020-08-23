import random

MIN_RANDOM_NUMBER_RANGE = 1
MAX_RANDOM_NUMBER_RANGE = 3
MIN_RANDOM_NUMBER_COUNT = 1
MAX_RANDOM_NUMBER_COUNT = 6


number_of_quick_picks = int(input("How many quick picks do you want? "))
for i in range(1, number_of_quick_picks + 1):
    quick_picks = []
    for j in range(MIN_RANDOM_NUMBER_COUNT, MAX_RANDOM_NUMBER_RANGE + 1):
        generated_result = random.randint(MIN_RANDOM_NUMBER_RANGE, MAX_RANDOM_NUMBER_RANGE + 1)
        while generated_result in quick_picks:
            generated_result = random.randint(MIN_RANDOM_NUMBER_RANGE, MAX_RANDOM_NUMBER_RANGE + 1)
        quick_picks.append(generated_result)
    quick_picks.sort()
    # print(quick_picks)
    print(" ".join("{:2}".format(generated_result) for generated_result in quick_picks))
