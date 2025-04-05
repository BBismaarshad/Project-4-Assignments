def main():
    phonebook = {}
    while True:
        print("\nPhonebook Options:")
        print("1. Add a contact")
        print("2. View all contacts")
        print("3. Delete a contact")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            name = input("Enter the contact's name: ").strip()
            number = input("Enter the contact's phone number: ").strip()
            phonebook[name] = number
            print(f"Contact '{name}' added successfully.")
        
        elif choice == '2':
            if not phonebook:
                print("Phonebook is empty.")
            else:
                print("\nContacts in the phonebook:")
                for name, number in phonebook.items():
                    print(f"{name}: {number}")
        
        elif choice == '3':
            name = input("Enter the contact's name to delete: ").strip()
            if name in phonebook:
                del phonebook[name]
                print(f"Contact '{name}' deleted successfully.")
            else:
                print(f"Contact '{name}' not found in the phonebook.")
        
        elif choice == '4':
            print("Exiting the phonebook. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()