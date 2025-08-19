#2348 - Number of Zero-Filled Subarrays

class Solution(object):
    def zeroFilledSubarray(self, nums):
        current_streak = 0
        total_subarrays = 0

        for num in nums:
            if num == 0:
                current_streak += 1
                total_subarrays += current_streak
            else:
                current_streak = 0
        return total_subarrays

# 2348. Number of Zero-Filled Subarrays
# Given an integer array nums, return the number of subarrays filled with 0.
# A subarray is a contiguous non-empty sequence of elements within an array.
# Example 1:
# Input: nums = [1,3,0,0,2,0,0,4]
# Output: 6
# Explanation: 
# There are 4 occurrences of [0] as a subarray.
# There are 2 occurrences of [0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
