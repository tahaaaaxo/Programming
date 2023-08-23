def set_cover(universe, subsets):
    # Create an empty list to store the chosen subsets
    chosen_subsets = []
    # Create a set to keep track of the remaining elements to be covered
    remaining_elements = set(universe)

    # Loop until all elements are covered
    while remaining_elements:
        # Choose the subset that covers the most uncovered elements
        best_subset = max(subsets, key=lambda subset: len(
            remaining_elements.intersection(subset)))
        # Add the chosen subset to the list of chosen subsets
        chosen_subsets.append(best_subset)
        # Remove the covered elements from the remaining elements set
        remaining_elements.difference_update(best_subset)

    return chosen_subsets


# Example usage
universe = set(range(1, 11))
subsets = [
    set([1, 2, 3, 4, 5]),
    set([4, 5, 6, 7]),
    set([7, 8, 9, 10]),
    set([2, 3, 6, 9])
]
chosen_subsets = set_cover(universe, subsets)
print("Chosen subsets are : ", chosen_subsets)
