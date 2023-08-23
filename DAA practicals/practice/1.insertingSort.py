def InsertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key


array_exp = [3, 2, 1, 7, 4, 6]
InsertionSort(array_exp)
print(array_exp)
