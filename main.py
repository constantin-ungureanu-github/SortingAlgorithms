import random
import time
from heap_sort import heap_sort
from insert_sort import insert_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from select_sort import select_sort
from shell_sort import shell_sort


def test_sort(sort, input_list, message):
    local_list = list(input_list)
    start_time = time.time()
    sort(local_list)
    end_time = time.time()
    print(message)
    print(local_list)
    print(end_time - start_time, "sec\n")

random_list = random.sample(range(1000000), 10000)
print(random_list)
print()

test_sort(bubble_sort, random_list, "Bubble Sort")
test_sort(heap_sort, random_list, "Heap Sort")
test_sort(insert_sort, random_list, "Insert Sort")
test_sort(merge_sort, random_list, "Merge Sort")
test_sort(quick_sort, random_list, "Quick Sort")
test_sort(select_sort, random_list, "Select Sort")
test_sort(shell_sort, random_list, "Shell Sort")
