# Given an array arr, return the second largest distinct element from an array.
# If the second largest element doesn't exist then return -1.

# brute force
# logic -- sort the array and last element will be the largest and second last will be yje secondlargest
# sort(arr) --> len(arr)-1 == largest,len(arr)-2 == secondlargest

# todo
# problem with this solution is that if list conatins same element then there is no 
# second largest and need to return -1
class Solution:
    def print2largest(self, arr):

        arr = sorted(arr)
        return arr[len(arr)-2]


# better solution

# logic -- 2 pass solution. in first pass finding the largest element amon the list and 
# in second pass finding the new maximum while checking that it is less than previous maximum

class Solution:
    def print2largest(self, arr):
        # Code Here
        maximum = arr[0]
        for i in range(1,len(arr)):
            if arr[i] > maximum:
                maximum = arr[i]
        newmax = None
        for i in range(len(arr)):
            if arr[i]!=maximum and (newmax is None or arr[i]>newmax):
                newmax = arr[i]
        return newmax if newmax is not None else -1


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends