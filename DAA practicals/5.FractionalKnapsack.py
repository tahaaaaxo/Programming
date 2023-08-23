def fractional_knapsack(items, capacity):
    # Calculate the ratio of value to weight for each item
    for item in items:
        item['ratio'] = item['value'] / item['weight']

    # Sort the items in decreasing order of their value-to-weight ratio
    items.sort(key=lambda item: item['ratio'], reverse=True)

    # Initialize the total value and weight of the knapsack
    total_value = 0
    total_weight = 0

    # Iterate over the sorted items and add them to the knapsack until it is full
    for item in items:
        if total_weight + item['weight'] <= capacity:
            total_value += item['value']
            total_weight += item['weight']
        else:
            fraction = (capacity - total_weight) / item['weight']
            total_value += fraction * item['value']
            total_weight += fraction * item['weight']
            break

    return total_value


items = [{'value': 60, 'weight': 10}, {
    'value': 100, 'weight': 20}, {'value': 120, 'weight': 30}]
capacity = 50
result = fractional_knapsack(items, capacity)
print(
    f"Maximum value that can be put into knapsack of capacity {capacity} is: {result}")
