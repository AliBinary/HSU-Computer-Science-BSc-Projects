def bounded_knapsack(weights, values, counts, capacity):
    # Number of items
    n = len(weights)

    # Create a DP array to store the maximum value for each capacity
    dp = [0] * (capacity + 1)

    # Create an array to track the items chosen
    chosen_items = [[0] * (capacity + 1) for _ in range(n)]

    # Process each item
    for i in range(n):
        for _ in range(counts[i]):
            for w in range(capacity, weights[i] - 1, -1):
                if dp[w] < dp[w - weights[i]] + values[i]:
                    dp[w] = dp[w - weights[i]] + values[i]
                    chosen_items[i][w] = chosen_items[i][w - weights[i]] + 1

    # Reconstruct the items selected
    selected_items = [0] * n
    remaining_capacity = capacity
    for i in range(n - 1, -1, -1):
        selected_items[i] = chosen_items[i][remaining_capacity]
        remaining_capacity -= selected_items[i] * weights[i]

    # Return the maximum value and the items chosen
    return dp[capacity], selected_items


def main():
    # Get the number of items
    n = int(input("Enter the number of items: "))

    # Get the weights, values, and counts of the items
    weights = []
    values = []
    counts = []

    print("\nEnter the details of each item:")
    for i in range(n):
        weight = int(input(f"Weight of item {i+1}: "))
        value = int(input(f"Value of item {i+1}: "))
        count = int(input(f"Maximum count of item {i+1}: "))
        weights.append(weight)
        values.append(value)
        counts.append(count)
        print()

    # Get the capacity of the knapsack
    capacity = int(input("Enter the capacity of the knapsack: "))

    # Call the bounded knapsack function
    max_value, selected_items = bounded_knapsack(
        weights, values, counts, capacity)

    # Output the result
    print(f"\nMaximum value in Bounded Knapsack: {max_value}")
    print("Items selected:")
    for i in range(n):
        if selected_items[i] > 0:
            print(f"Item {i+1}: {selected_items[i]} times")


# Run the main function
if __name__ == "__main__":
    main()
