def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    return low <= n <= high

def main():
    # Example usage of the in_range function
    print(in_range(5, 1, 10))  # Should print True
    print(in_range(15, 1, 10))  # Should print False
    print(in_range(10, 1, 10))  # Should print True

if __name__ == '__main__':
    main()