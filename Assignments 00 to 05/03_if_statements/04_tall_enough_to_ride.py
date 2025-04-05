def main():
    min_height = 50
    height_input = input("How tall are you? ")
    if height_input.strip() == "":
        return
    height = int(height_input)
    if height >= min_height:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

def tall_enough_extension():
    min_height = 50
    while True:
        height_input = input("How tall are you? ")
        if height_input.strip() == "":
            break
        height = int(height_input)
        if height >= min_height:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()
    # Uncomment the next line to run the extended version
    # tall_enough_extension()