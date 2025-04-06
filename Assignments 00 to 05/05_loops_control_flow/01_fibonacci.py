def main():
    MAX_VALUE = 10000
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    # Print the first two numbers
    print(a, end=' ')
    if b < MAX_VALUE:
        print(b, end=' ')
    # Generate and print subsequent numbers until exceeding MAX_VALUE
    while True:
        next_term = a + b
        if next_term >= MAX_VALUE:
            break
        print(next_term, end=' ')
        a, b = b, next_term
    print()  # For a new line at the end

if __name__ == '__main__':
    main()