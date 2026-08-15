class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minPos = 1

        for num in nums[1:]:
            if num < minPos and num > 0:
                minPos = num

        if (minPos-1) > 0:
            return minPos-1

        if minPos in nums:
            minPos+=1

        while (minPos) in nums:
            minPos+=1

        return minPos