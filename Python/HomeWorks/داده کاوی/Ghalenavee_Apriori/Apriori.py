from itertools import combinations, chain


def frequent_itemsets(transactions, support_threshold):
    item_counts = {}
    for transaction in transactions:
        for item in transaction:
            item_counts[item] = item_counts.get(item, 0) + 1
    frequent_items = {item: count for item, count in item_counts.items(
    ) if count/len(transactions) >= support_threshold}
    frequent_itemsets = frequent_items.copy()
    k = 2
    while frequent_itemsets:
        candidate_itemsets = set(combinations(frequent_itemsets.keys(), k))
        item_counts = {itemset: 0 for itemset in candidate_itemsets}
        for transaction in transactions:
            for itemset in candidate_itemsets:
                if set(itemset).issubset(transaction):
                    item_counts[itemset] += 1
        frequent_itemsets = {itemset: count for itemset, count in item_counts.items(
        ) if count/len(transactions) >= support_threshold}
        frequent_items.update(frequent_itemsets)
        k += 1
    return frequent_items


# Example usage
transactions = [
    ['apple', 'banana', 'pear'],
    ['banana', 'pear', 'orange'],
    ['pear', 'orange'],
    ['apple', 'pear'],
    ['apple', 'banana', 'pear', 'orange']
]

frequent_itemsets = frequent_itemsets(transactions, support_threshold=0.6)
print(frequent_itemsets)
