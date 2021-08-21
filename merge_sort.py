import random
import time

class MergeSort():

    def merger(self,u_list, start_index, divider, end_index):
        n1 = divider - start_index + 1
        n2 = end_index - divider
        L = []
        R = []
        i = 0
        j = 0
        A = []

        while i < n1:
            L.append(u_list[start_index + i])
            i = i + 1

        while j < n2:
            R.append(u_list[divider + j + 1]) 
            j = j + 1

        R.append('end')
        L.append('end')
    
        i = 0
        j = 0
        k = start_index
        
        while k <= end_index:
            if(L[i] == 'end' and R[j] == 'end'):
                break
            if (L[i] != 'end' and R[j] != 'end' and (L[i] <= R[j])) or (R[j] == 'end'):
                A.append(L[i])
                i = i + 1
                k = k + 1
            elif (R[j] != 'end' and L[i] != 'end' and L[i] > R[j]) or (L[i] == 'end'):
                A.append(R[j])
                j = j + 1
                k = k + 1

        indexes = list(range(start_index,end_index + 1))
        for i in indexes:
            u_list[i] = A[i - start_index]
        
        return u_list

    

    def merge_sort(self, entry_list, start_index, end_index):
        if(start_index < end_index):
            half_index = (start_index + end_index) // 2
            entry_list = self.merge_sort(entry_list, start_index, half_index)
            entry_list = self.merge_sort(entry_list, half_index + 1, end_index)
            merged_list = self.merger(entry_list, start_index, half_index, end_index)
            # print(merged_list)
            indexes = list(range(start_index,end_index + 1))
            for i in indexes:
                entry_list[i] = merged_list[i]

            return entry_list
        else:
            return entry_list
sort = MergeSort()
un_ordered_list = list(range(0,100000))
end_index = len(un_ordered_list) - 1
start_time = time.time()
# for i in range(1,10):
random.shuffle(un_ordered_list)
# print('initial is : ', un_ordered_list) 
result = sort.merge_sort(un_ordered_list, 0, end_index)

print("--- %s seconds ---" % (time.time() - start_time))