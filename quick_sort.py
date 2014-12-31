def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)


def quick_sort_helper(array, first, last):
    if first < last:
        gap = partition(array, first, last)
        quick_sort_helper(array, first, gap - 1)
        quick_sort_helper(array, gap + 1, last)


def partition(array, first, last):
    pivot = array[first]
    left = first + 1
    right = last

    done = False
    while not done:

        while left <= right and array[left] <= pivot:
            left += 1

        while array[right] >= pivot and right >= left:
            right -= 1

        if right < left:
            done = True
        else:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp

    temp = array[first]
    array[first] = array[right]
    array[right] = temp
    return right