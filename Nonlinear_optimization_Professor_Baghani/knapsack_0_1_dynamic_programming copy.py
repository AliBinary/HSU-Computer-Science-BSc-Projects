import os


def clrscr():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def knapsack(weights, values, capacity):
    # Number of items
    n = len(weights)

    # Create a 2D DP table to store the maximum value at each stage
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):  # Loop over items
        for w in range(1, capacity + 1):  # Loop over possible knapsack capacities
            if weights[i - 1] <= w:
                # Item can be included: take the max of including or excluding the item
                dp[i][w] = max(dp[i - 1][w], values[i - 1] +
                               dp[i - 1][w - weights[i - 1]])
            else:
                # Item can't be included: take the value without the item
                dp[i][w] = dp[i - 1][w]

    print(dp)

    # Backtrack to find the items included
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # This means item `i-1` is included
            selected_items.append(i)  # Add the item index
            # Reduce the capacity by the weight of the selected item
            w -= weights[i - 1]

    # Return the maximum value and the selected items
    return dp[n][capacity], selected_items


def main():
    # Get the number of items from the user
    n = int(input("Enter the number of items: "))

    # Get the weights and values of the items
    weights = []
    values = []

    print()
    for i in range(n):
        weight = int(input(f"Enter the weight of item {i + 1}: "))
        weights.append(weight)

    print()
    for i in range(n):
        value = int(input(f"Enter the value of item {i + 1}: "))
        values.append(value)

    # Get the capacity of the knapsack
    capacity = int(input("\nEnter the capacity of the knapsack: "))

    # Call the knapsack function
    result, selected_items = knapsack(weights, values, capacity)

    # Output the result
    print(f"\nMaximum value in Knapsack: {result}\n")
    print("Items selected:")
    for item in selected_items:
        print(f"Item {item}")


# Run the main function
if __name__ == "__main__":
    clrscr()
    main()
