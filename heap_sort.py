def heap_sort(array):
    size = len(array)
    heapify(array, size)
    end = size - 1
    while end > 0:
        swap(array, 0, end)
        siftdown(array, 0, end)
        end -= 1


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


def siftdown(array, i, size):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left <= size - 1 and array[left] > array[i]:
        largest = left
    if right <= size - 1 and array[right] > array[largest]:
        largest = right
    if largest != i:
        swap(array, i, largest)
        siftdown(array, largest, size)


def heapify(array, size):
    p = (size // 2) - 1
    while p >= 0:
        siftdown(array, p, size)
        p -= 1