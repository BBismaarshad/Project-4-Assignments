def get_last_element(lst):
    print(lst[-1])

def main():
    lst = []
    n = int(input("Enter the number of elements in the list: "))
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        lst.append(element)
    get_last_element(lst)

if __name__ == '__main__':
    main()