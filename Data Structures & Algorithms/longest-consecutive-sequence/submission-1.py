class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        vals = set(nums)
        longest = 1
    
        for val in vals:
            if not (val - 1) in vals:
                cur = val
                count = 1
                while (cur + count) in vals:
                    count+=1
                longest = max(count, longest)
        return longest
        