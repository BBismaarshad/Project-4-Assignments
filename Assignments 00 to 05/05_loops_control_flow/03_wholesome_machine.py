def main():
    affirmation = "I am capable of doing anything I put my mind to."
    print(f"Please type the following affirmation: {affirmation}")
    
    while True:
        user_input = input()
        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("That was not the affirmation. Please type the following affirmation:", affirmation)

if __name__ == '__main__':
    main()