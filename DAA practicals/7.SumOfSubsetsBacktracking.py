def sum_of_subsets(numbers, target_sum):
    # Create a list to store the current subset
    current_subset = []
    # Call the helper function with the initial state
    backtrack(numbers, target_sum, 0, 0, current_subset)


def backtrack(numbers, target_sum, current_sum, index, current_subset):
    # Base case: if the current sum equals the target sum, print the current subset
    if current_sum == target_sum:
        print(current_subset)
    # If the current sum is greater than the target sum or we've reached the end of the list, backtrack
    elif current_sum > target_sum or index == len(numbers):
        return
    else:
        # Recursive case: try including the current number and then backtrack
        current_subset.append(numbers[index])
        backtrack(numbers, target_sum, current_sum +
                  numbers[index], index + 1, current_subset)
        current_subset.pop()
        # Try excluding the current number and then backtrack
        backtrack(numbers, target_sum, current_sum, index + 1, current_subset)


# Example usage
numbers = [10, 7, 5, 18, 12, 20, 15]
target_sum = 35
sum_of_subsets(numbers, target_sum)
