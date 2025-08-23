from typing import List

# nums = [1, 2, 3, 1]

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1]:
#                 return True
#         return False
    
    # ALTERNATIVE MORE EFFICIENT SOLUTON WITH THE INBUILT SET FUNCTION 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = set(nums)
        return len(dup) != len(nums)