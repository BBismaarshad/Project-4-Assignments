# def feet_to_inches(feet):
#     return feet * 12
# def main():
#     print("Feet to Inches Converter")
#     print("-----------------------")
#     while True: 
#         user_input = input("Enter length in feet (or 'q' to quit): ").strip()
#         if user_input.lower() in ["q","quit"]:
#             print("Goodbye!")
#             break
#         try:
#             feet = float(user_input)
#            # Calculate inches
#             inches = feet_to_inches(feet)
            
#             # Handle singular/plural forms
#             foot_unit = "foot" if feet == 1 else "feet"
#             inch_unit = "inch" if inches == 1 else "inches"

#             # Display result
#             print(f"\n{feet} {foot_unit} = {inches} {inch_unit}\n")
            
#         except ValueError:
#             print("Invalid input. Please enter a number or 'q' to quit.\n")

# if __name__ == '__main__':
#     main()




"""
An example program with constants
"""

INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

def main():
    feet: float = float(input("Enter number of feet: "))  # Get the number of feet, make sure to cast it to a float!
    inches: float = feet * INCHES_IN_FOOT  # Perform the conversion
    print("That is", inches, "inches!")
    
    
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()