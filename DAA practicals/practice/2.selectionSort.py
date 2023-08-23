
def selectionSort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)-1):
            if array[j] > array[min_idx]:
                min_idx = j
            array[min_idx], array[j] = array[j], array[min_idx]


array_exp = [3, 2, 1, 7, 4, 6]
# selectionSort(array_exp)
array_exp.sort()
print(array_exp.find)


# for i in range(len(array)):
#         min_idx = i
#         for j in range(i+1, len(array)-1):
#             if array[j] < array[min_idx]:
#                 min_idx = j
#             array[min_idx], array[i] = array[i], array[min_idx]
