def select_sort(array):
    for index in range(len(array) - 1, 0, -1):
        index_max = 0
        for location in range(1, index + 1):
            if array[location] > array[index_max]:
                index_max = location

        temp = array[index]
        array[index] = array[index_max]
        array[index_max] = temp
