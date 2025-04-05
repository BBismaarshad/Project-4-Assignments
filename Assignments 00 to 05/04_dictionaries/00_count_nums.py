def main():
    numbers = []
    while True:
        user_input = input("Enter a number: ").strip()
        if not user_input:
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number.")
    
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    
    for number in sorted(counts.keys()):
        print(f"{number} appears {counts[number]} times.")

if __name__ == '__main__':
    main()