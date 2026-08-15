class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minPos = 1
        
        if minPos in nums:
            minPos+=1

        while minPos in nums:
            minPos += 1

        return minPos