import random

def find_num(x, guess):
    if 0 < guess < 11: # 12
        if guess == x: # 2 == 2
            print('Вы гений')
            return True
    else:
        print('enter number in range 1-10')
        return False
    

x = random.randint(1, 10)
# ! if __name__ == "__main__":
while True:
    guess = int(input('find a secret number in range of 1-10: ')) # int('a')
    if guess == x:
        break
    