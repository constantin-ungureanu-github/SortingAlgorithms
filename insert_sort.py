def insert_sort(array):
    for i in range(1, len(array)):
        value = array[i]
        j = i

        while j > 0 and array[j-1] > value:
            array[j] = array[j-1]
            j -= 1

        array[j] = value