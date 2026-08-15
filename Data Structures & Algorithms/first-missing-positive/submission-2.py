class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not 1 in nums:
            return 1

        n = len(nums)

        i = 0
        while i < n:
            if nums[i] <= 0 or nums[i] > n:
                i += 1
                continue

            new_idx = nums[i] - 1
            if nums[i] != nums[new_idx]:
                nums[i], nums[new_idx] = nums[new_idx], nums[i]
            else:
                i += 1


        for i in range(n):
            if not nums[i] == i+1:
                return i+1
        
        return n+1
