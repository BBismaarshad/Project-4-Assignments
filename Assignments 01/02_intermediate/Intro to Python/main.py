GRAVITY_MULTIPLIERS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def main():
    earth_weight = float(input("Enter a weight on Earth: "))

  
    planet = input("Enter a planet: ")

   
    gravity = GRAVITY_MULTIPLIERS[planet]

    
    planetary_weight = round(earth_weight * gravity, 2)

    
    print(f"The equivalent weight on {planet}: {planetary_weight}")


if __name__ == "__main__":
    main()
