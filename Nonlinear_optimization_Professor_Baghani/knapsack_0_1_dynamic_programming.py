import os


def clrscr():
    if (os.name == 'posix'):
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
            if weights[i-1] <= w:
                # Item can be included: take the max of including or excluding the item
                dp[i][w] = max(dp[i-1][w], values[i-1] +
                               dp[i-1][w - weights[i-1]])
            else:
                # Item can't be included: take the value without the item
                dp[i][w] = dp[i-1][w]

    # Return the maximum value that can be obtained with the given capacity
    return dp[n][capacity]


def main():
    # Get the number of items from the user
    n = int(input("Enter the number of items: "))

    # Get the weights and values of the items
    weights = []
    values = []

    print()
    for i in range(n):
        weight = int(input(f"Enter the weight of item {i+1}: "))
        weights.append(weight)

    print()
    for i in range(n):
        value = int(input(f"Enter the value of item {i+1}: "))
        values.append(value)

    # Get the capacity of the knapsack
    capacity = int(input("\nEnter the capacity of the knapsack: "))

    # Call the knapsack function
    result = knapsack(weights, values, capacity)

    # Output the result
    print(f"Maximum value in Knapsack: {result}\n")


# Run the main function
if __name__ == "__main__":
    clrscr()
    main()
