def MergeSort(array):
    if len(array) <= 1:
        return array

    mid = len(array)//2
    left_side = array[:mid]
    right_side = array[mid:]

    sorted_left_side = MergeSort(left_side)
    sorted_right_side = MergeSort(right_side)

    sorted_numbers = []
    i = j = 0
    while i < len(sorted_left_side) and j < len(right_side):
        if sorted_left_side[i] < sorted_right_side[j]:
            sorted_numbers.append(sorted_left_side[i])
            i += 1
        else:
            sorted_numbers.append(sorted_right_side[j])
            j += 1
    sorted_numbers += sorted_left_side[i:]
    sorted_numbers += sorted_right_side[:i]


array = [3, 2, 1, 7, 4, 6]
num = MergeSort(array)
print(num)
