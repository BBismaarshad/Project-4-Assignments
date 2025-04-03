def main():
    # Speed of light in m/s (constant)
    C = 299792458

    while True:
        # Ask the user for mass in kilograms
        mass_input = input("Enter kilos of mass (or 'quit' to exit): ")

        # Check if the user wants to quit
        if mass_input.lower() == 'quit':
            print("Exiting the program. Goodbye!")
            break

        try:
            # Convert the input to a float
            mass = float(mass_input)

            # Calculate energy using E = m * c^2
            energy = mass * (C ** 2)

            # Display the result
            print("\ne = m * C^2...")
            print(f"m = {mass} kg")
            print(f"C = {C} m/s")
            print(f"{energy} joules of energy!\n")

        except ValueError:
            print("Invalid input. Please enter a valid number or 'quit' to exit.\n")

if __name__ == '__main__':
    main()