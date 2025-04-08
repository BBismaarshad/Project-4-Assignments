def count_even():
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            num = int(user_input)
            lst.append(num)
        except ValueError:
            print("Please enter a valid integer or press enter to stop.")
    
    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
    print(even_count)

def main():
    count_even()

if __name__ == '__main__':
    main()