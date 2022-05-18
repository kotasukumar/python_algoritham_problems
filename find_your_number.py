import random


def magic_number(range):
    random_number = random.randint(0, range - 1)
    print(random_number)
    n = range
    while random_number != n:
        n = int(input("Enter the number: "))
        if n > random_number:
            print("Entered number is greater then generated number")
        if n < random_number:
            print("Entered number is lesser then generated number")
        if n == random_number:
            print("your guess is correct")


if __name__ == "__main__":
    range = int(input("Enter value of range: "))
    magic_number(range)

