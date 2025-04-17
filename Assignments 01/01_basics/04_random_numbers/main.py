import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    Generates and prints 10 random numbers between 1 and 100, each time producing different numbers.
    """
    for i in range(N_NUMBERS):
        num = random.randint(MIN_VALUE, MAX_VALUE)
        print(num, end=' ')
    print()  # Ensure a new line after the numbers

if __name__ == '__main__':
    main()