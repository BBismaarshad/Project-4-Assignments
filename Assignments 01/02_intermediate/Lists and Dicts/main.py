def main():
    # Problem #1: List Practice
    print("=== List Practice ===")
    # Create a list called `fruit_list` that contains the following fruits:
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list.
    print("Length of fruit list:", len(fruit_list))

    # Add 'mango' at the end of the list.
    fruit_list.append('mango')

    # Print the updated list.
    print("Updated fruit list:")
    for fruit in fruit_list:
        print(fruit)

# =============================
# Problem #2: Index Game
# =============================

def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    # Python slicing already handles out-of-range values safely,
    # but we'll still check if the indices are valid types.
    if not (isinstance(start, int) and isinstance(end, int)):
        return "Invalid indices."
    return lst[start:end]

def index_game():
    lst = [1, 2, 3, 4, 5]  # Example list
    print("\n=== Index Game ===")
    print("Current list:", lst)

    while True:
        print("\nChoose an operation: access, modify, slice, or exit")
        operation = input("Enter operation: ").strip().lower()

        if operation == "access":
            index = int(input("Enter index to access: "))
            print("Element at index:", access_element(lst, index))

        elif operation == "modify":
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            try:
                new_value = int(new_value)  # Try converting to integer
            except ValueError:
                pass  # Leave as string if not an integer
            result = modify_element(lst, index, new_value)
            print("Updated list:", result)

        elif operation == "slice":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced list:", slice_list(lst, start, end))

        elif operation == "exit":
            print("Exiting game.")
            break

        else:
            print("Invalid operation. Try again.")

# =============================
# Run the programs
# =============================

if __name__ == '__main__':
    main()
    index_game()
