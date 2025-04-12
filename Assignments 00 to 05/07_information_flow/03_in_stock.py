def main():
    fruit = input("Enter a fruit: ")
    quantity = num_in_stock(fruit)
    if quantity > 0:
        print("This fruit is in stock! Here is how many:")
        print(quantity)
    else:
        print("This fruit is not in stock.")

# The following function is assumed to be predefined in the problem's context.
def num_in_stock(fruit):
    # This is a placeholder for the actual implementation.
    # The actual function would presumably have an inventory dictionary or database lookup.
    # For example:
    inventory = {
        'apple': 50,
        'banana': 30,
        'pear': 1000,
        'orange': 75
    }
    return inventory.get(fruit.lower(), 0)

if __name__ == '__main__':
    main()