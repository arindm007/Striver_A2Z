# brute force

# Given an array arr[] sorted in ascending order of size N and an integer K.
#  Check if K is present in the array or not.

# applying linear serch over the array...tryversing the array and comapring with the target element


class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        for i in range(N):
            if arr[i] == K:
                return 1
        return -1