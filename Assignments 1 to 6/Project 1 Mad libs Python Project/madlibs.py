print("Welcome to Mad Libs - Computer Programming Edition!")
print("Please enter the following words to complete the story:\n")

adj = input("Enter an adjective (e.g., amazing, challenging): ")
verb1 = input("Enter a verb (e.g., code, create): ")
verb2 = input("Enter another verb (e.g., dance, innovate): ")
famous_person = input("Enter a famous person's name (e.g., Elon Musk, Ada Lovelace): ")

madlib = f"\nComputer programming is so {adj}! It makes me excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you're {famous_person}!\n"

print(madlib)
print("Thanks for playing Mad Libs!")