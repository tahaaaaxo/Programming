def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        print(array)
        left_side = []
        righ_side = []
        pivot = array[0]
        # print(pivot)

        for i in range(1, len(array)):
            if array[i] < pivot:
                left_side.append(array[i])
            else:
                righ_side.append(array[i])
        print(left_side, righ_side)

    sorted_left = quicksort(left_side)
    sorted_right = quicksort(righ_side)
    X = []
    X == ([sorted_left]+[pivot]+[sorted_right])

    return X


array = [3, 2, 5, 1, 4, 7, 6]
print(quicksort(array))
