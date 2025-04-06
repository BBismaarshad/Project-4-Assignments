def main():
    # Ask the user to enter a number
    num = int(input("Enter a number: "))
    curr_value = num
    # Loop until curr_value is 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=' ')

if __name__ == '__main__':
    main()