def main():
    result = []
    for num in range(10, 20):
        if num % 2 == 0:
            result.append(f"{num} even")
        else:
            result.append(f"{num} odd")
    print(' '.join(result))

if __name__ == '__main__':
    main()