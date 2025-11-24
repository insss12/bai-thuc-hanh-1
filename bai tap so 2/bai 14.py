import random

random_number=random.randint(1, 10)
while True:
    test = int(input())
    if test < random_number:
        print("lonws hon")
        continue
    elif test > random_number:
        print("be hon")
        continue
    else:
        print("correct")
        break