class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        current_streak = 0 
        prev_streak = 0 

        for num in nums:
            if num == 1 :
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak+prev_streak)

                prev_streak = current_streak
                current_streak = 0
        longest_streak = max(longest_streak, current_streak+prev_streak)

        if longest_streak == len(nums):
            return longest_streak - 1
        return longest_streak
