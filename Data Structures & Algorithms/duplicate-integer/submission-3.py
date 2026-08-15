class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size = len(nums)
        numSet = set(nums)
        setsize = len(numSet)

        if size == setsize:
            return False
        return True
