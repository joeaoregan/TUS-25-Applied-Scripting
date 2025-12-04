# Variable Arguments in Functions

def calc_total_cost(*prices):
    """Calculate the total cost of any number of items."""
    return sum(prices)

if __name__ == "__main__":
    # You can pass any number of item prices
    print(f"Cost of 3 items: {calc_total_cost(19.99, 5.49, 3.50):.2f}") # 28.98
    print(f"Cost of 2 items: {calc_total_cost(12.00, 7.50):.2f}") # 19.50