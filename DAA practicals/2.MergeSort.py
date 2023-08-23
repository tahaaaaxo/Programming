def merge_sort(numbers):
    # Base case: the list is empty or has one element
    if len(numbers) <= 1:
        return numbers

    # Divide the list into two halves
    mid = len(numbers) // 2
    left_half = numbers[:mid]
    right_half = numbers[mid:]

    # Recursively apply merge sort to each half
    sorted_left_half = merge_sort(left_half)
    sorted_right_half = merge_sort(right_half)

    # Merge the sorted halves
    sorted_numbers = []
    i = j = 0
    while i < len(sorted_left_half) and j < len(sorted_right_half):
        if sorted_left_half[i] < sorted_right_half[j]:
            sorted_numbers.append(sorted_left_half[i])
            i += 1
        else:
            sorted_numbers.append(sorted_right_half[j])
            j += 1
    sorted_numbers += sorted_left_half[i:]
    sorted_numbers += sorted_right_half[j:]

    return sorted_numbers


# Example usage
numbers = [5, 2, 9, 1, 5, 6, 8, 3]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)
