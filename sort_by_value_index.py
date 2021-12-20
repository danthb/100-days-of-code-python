def sort_by_value_and_index(arr):
    arr_aux = []
    new_arr = []
    for i in range(len(arr)):
        arr_aux.append(arr[i] * (i+1))
    for j in range(len(arr_aux)):
        index_smallest = find_smallest(arr_aux)
        new_arr.append(arr.pop(index_smallest))
        arr_aux.pop(index_smallest)
    return new_arr


def find_smallest(arr_aux):
    smallest = arr_aux[0]
    index_smallest = 0
    for i in range(1, len(arr_aux)):
        if arr_aux[i] < smallest:
            smallest = arr_aux[i]
            index_smallest = i
    return index_smallest


print(sort_by_value_and_index([1, 2, 3, 4, 5]))
print(sort_by_value_and_index([23, 2, 3, 4, 5]))

"""  [ 2, 3, 4, 23, 5 ] """
