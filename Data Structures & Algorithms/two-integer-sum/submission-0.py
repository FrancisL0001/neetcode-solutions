class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            val = target - nums[i]
            if val in seen:
                return [seen[val], i]
            else:
                seen[nums[i]] = i
        
        return [-1, -1]