import time
import random

my_list = [31, 41, 59, 26, 41, 58]
my_list = list(range(0, 100000))
start_time = time.time()
# for i in range(1, 100):
random.shuffle(my_list)
my_list.sort()
print("--- %s seconds ---" % (time.time() - start_time))