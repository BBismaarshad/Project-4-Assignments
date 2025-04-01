def main():
    print("Triangle Perimeter Calculator")
    print("----------------------------")
    
    # Get user input for each side, converting to float to handle decimals
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))
    
    # Calculate perimeter by summing all sides
    perimeter = side1 + side2 + side3
    
    # Display the result with formatting that matches the sample output
    print(f"\nThe perimeter of the triangle is {perimeter}")

if __name__ == "__main__":
    main()