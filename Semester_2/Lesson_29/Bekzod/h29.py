import random

x=random.randint(1,10)

def find_num(guess):
    if 0 < guess < 11:
        if guess == x:
            print("Вы гений")
            return True
    else:
        print("Enter number range 1-10")
        return False

# ! if __name__ == "__main__":
while True:
    guess = int(input("Find secret number in range 1-10: "))
    if find_num(guess):
        break