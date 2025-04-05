def main():
    fruit_prices = {
        'apple': 1.0,
        'durian': 15.0,
        'jackfruit': 10.0,
        'kiwi': 2.5,
        'rambutan': 5.0,
        'mango': 3.0
    }
    
    total_cost = 0.0
    
    for fruit in fruit_prices:
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += quantity * fruit_prices[fruit]
    
    print(f"Your total is ${total_cost:.1f}")

if __name__ == '__main__':
    main()