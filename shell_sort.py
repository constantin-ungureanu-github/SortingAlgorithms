def shell_sort(array):
    count = len(array) // 2
    while count > 0:
        for start in range(count):
            gap_sort(array, start, count)
        count //= 2


def gap_sort(array, start, gap):
    for i in range(start+gap, len(array), gap):
        value = array[i]
        position = i

        while position >= gap and array[position-gap] > value:
            array[position] = array[position-gap]
            position -= gap

        array[position] = value