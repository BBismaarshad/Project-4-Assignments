def double(num):
    return num * 2

def main():
    num = float(input("Enter a number: "))
    result = double(num)
    print(f"Double that is {result}")

if __name__ == '__main__':
    main()