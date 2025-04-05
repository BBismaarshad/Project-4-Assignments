d# Function to add three copies of the given data to the list
def add_three_copies(lst, data):
    for _ in range(3):  # Loop three times
        lst.append(data)  # Append the data to the list each time

# Main function to demonstrate the effect of modifying a mutable list
def main():
    my_list = []  # Initialize an empty list
    message = input("Enter a message to copy: ")  # Get user input for the message
    print(f"List before: {my_list}")  # Print the list before modification
    add_three_copies(my_list, message)  # Call the function to modify the list
    print(f"List after: {my_list}")  # Print the list after modification

# Standard boilerplate to call the main function
if __name__ == '__main__':
    main()