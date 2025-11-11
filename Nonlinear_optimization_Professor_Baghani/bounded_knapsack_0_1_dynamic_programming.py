def bounded_knapsack(weights, values, counts, capacity):
    # Number of items
    n = len(weights)

    # Create a DP array to store the maximum value for each capacity
    dp = [0] * (capacity + 1)

    # Process each item
    for i in range(n):
        # Process the item `counts[i]` times
        for _ in range(counts[i]):
            # Update DP array from high to low capacity to avoid overwriting
            for w in range(capacity, weights[i] - 1, -1):
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    # Return the maximum value that can be obtained with the given capacity
    return dp[capacity]


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
    result = bounded_knapsack(weights, values, counts, capacity)

    # Output the result
    print(f"\nMaximum value in Bounded Knapsack: {result}")


# Run the main function
if __name__ == "__main__":
    main()
