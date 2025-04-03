def main():
    # Prompt the user for an adjective, noun, and verb
    adjective = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter. ")
    verb = input("Please type a verb and press enter. ")
    
    # Construct the sentence using the user's inputs
    sentence = f"The {adjective} {noun} {verb} over the lazy dog."
    
    # Print the constructed sentence
    print(sentence)

if __name__ == '__main__':
    main()


