MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(removed_item)

def main():
    lst = []
    print("Enter the elements of the list one by one. Press enter on an empty line to finish.")
    while True:
        element = input("Enter an element: ")
        if element == "":
            break
        lst.append(element)
    shorten(lst)
    print("Final list:", lst)

if __name__ == '__main__':
    main()