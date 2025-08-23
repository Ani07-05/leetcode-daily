class Solution(object):
    def runningSum(self, nums):
        runningScore = []
        total = 0 

        for num in nums:
            total += num 
            runningScore.append(total)
        return runningScore      