import random

def main():
    for _ in range(10):
        print(random.randint(1, 100), end=' ')
    print()  # To ensure the output ends with a new line

if __name__ == '__main__':
    main()