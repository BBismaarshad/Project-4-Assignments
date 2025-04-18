def main():
    # Ask the user to enter a number
    num = int(input("Enter a number: "))
    
    # Initialize curr_value with the entered number
    curr_value = num
    
    # Double the number until it's 100 or greater
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=' ')
    
    print()  # Print a newline at the end

if __name__ == '__main__':
    main()