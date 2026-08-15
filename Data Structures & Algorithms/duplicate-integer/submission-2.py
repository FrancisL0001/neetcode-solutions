class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in range(len(nums)):
            if not nums[i] in seen:
                seen[nums[i]] = i
            else:
                return True
        return False
