# Messages
PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY: str = "Sorry I only tell jokes."

def main():
    # Ask user what they want
    user_input = input(PROMPT)
    
    # Clean the input (remove extra spaces and make lowercase)
    user_input = user_input.strip().lower()
    
    # Check if user asked for a joke
    if "joke" in user_input:
        print(JOKE)  # Tell the joke
    else:
        print(SORRY)  # Say sorry

# Start the program
if __name__ == "__main__":
    main()