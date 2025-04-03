def main():
    # Prompt the user for the dividend and divisor
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))
    
    # Calculate the quotient and remainder
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    # Output the result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    main()