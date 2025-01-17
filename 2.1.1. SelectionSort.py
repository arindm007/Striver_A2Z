# Sorting Series Implemention all different type of sorting algorithms 
# Implementation of Selection sort

# The algorithm repeatedly selects the smallest (or largest) element 
# from the unsorted portion of the list and swaps it with the first 
# element of the unsorted part. This process is repeated for the 
# remaining unsorted portion until the entire list is sorted. 



class Solution:

    def __init__(self) -> None:
        pass
    
    def swap(self,arr:list,idx1:int,idx2:int):
        temp = arr[idx1]
        arr[idx1] = arr[idx2]
        arr[idx2] = temp
        return arr

    def selectionsort(self,arr:list):

        
        for i in range(len(arr)-1):
            mini = i
            for j in range(i,len(arr)):
                if arr[j]<arr[mini]:
                    mini = j
            self.swap(arr,mini,i)
        return arr


if __name__ == "__main__":
    sol = Solution()
    print(sol.selectionsort([13,46,24,51,20,9]))