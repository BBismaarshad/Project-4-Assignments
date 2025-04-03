import math

def main():
    # Prompt the user for the lengths of AB and AC
    ab_length = float(input("Enter the length of AB: "))
    ac_length = float(input("Enter the length of AC: "))
    
    # Calculate the hypotenuse BC using the Pythagorean theorem
    bc_length = math.sqrt(ab_length ** 2 + ac_length ** 2)
    
    # Output the result
    print(f"The length of BC (the hypotenuse) is: {bc_length}")

if __name__ == '__main__':
    main()