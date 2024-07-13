# Given an array arr, the task is to find the largest element in it.


from typing import List

# Brute force

# logic -- Sort the array in ascending and the last element will be the largest
# for the index of last element = len(arr)-1

class Solution:
    def largest(self, n : int, arr : List[int]) -> int:
        # code here
        arr = sorted(arr)
        return arr[len(arr)-1]
    
# Better solution

# logic -- store the first element as maximum and iterate over the list from the 1st element 
# and check if the elment in the list is greter then maximum then change the value of maximum  

class Solution:
    def largest(self, n : int, arr : List[int]) -> int:
        # code here
        maximum = arr[0]
        for i in range(1,len(arr)):
            if arr[i] > maximum:
                maximum = arr[i]
        return maximum


# Driver code of GFG
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = t

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.largest(n, arr)

        print(res)