# leetcode 1 Two sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# brute force

# logic -- two poiters approach iterating over the aray
            # use 2 loops to iterate over the array one over the entire array and other starting from index of first loop + 1th position 
            # if the sum of two elements are equal to target then just return the indices

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
 

#  TODO -Write the best and the optimal approach for the two sum problem

