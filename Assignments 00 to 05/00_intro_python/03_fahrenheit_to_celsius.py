def main():
    # Prompt the user for a temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert Fahrenheit to Celsius using the given formula
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    # Print the result with the specified format
    print(f"Temperature: {fahrenheit}F = {celsius}C")

# Call the main function
if __name__ == "__main__":
    main()