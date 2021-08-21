#insertion sort that is best practice for sorting arrays with small number of elements
import time
import random

# class Sort:
def InsertionSort(array):
    j = 1
    while j < len(array):
        key = array[j]
        i = j - 1
        while (i >= 0) and (array[i] > key):
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key
        j +=1
    return array
my_list = list(range(0, 10000))
start_time = time.time()
# for i in range(1, 10):
random.shuffle(my_list)
result = InsertionSort(my_list)
    
print("--- %s seconds ---" % (time.time() - start_time))

