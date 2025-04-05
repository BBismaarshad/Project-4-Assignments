def main():
    age = int(input("How old are you? "))
    
    peturksbouipo_age = 16
    stanlau_age = 25
    mayengua_age = 48
    
    # Check Peturksbouipo
    if age >= peturksbouipo_age:
        peturksbouipo_msg = f"You can vote in Peturksbouipo where the voting age is {peturksbouipo_age}."
    else:
        peturksbouipo_msg = f"You cannot vote in Peturksbouipo where the voting age is {peturksbouipo_age}."
    
    # Check Stanlau
    if age >= stanlau_age:
        stanlau_msg = f"You can vote in Stanlau where the voting age is {stanlau_age}."
    else:
        stanlau_msg = f"You cannot vote in Stanlau where the voting age is {stanlau_age}."
    
    # Check Mayengua
    if age >= mayengua_age:
        mayengua_msg = f"You can vote in Mayengua where the voting age is {mayengua_age}."
    else:
        mayengua_msg = f"You cannot vote in Mayengua where the voting age is {mayengua_age}."
    
    # Combine all messages
    result = f"{peturksbouipo_msg} {stanlau_msg} {mayengua_msg}"
    print(result)

if __name__ == '__main__':
    main()