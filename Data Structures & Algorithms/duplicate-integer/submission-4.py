class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size = len(nums)
        ## create a set that contains unique instances of all elements
        numSet = set(nums) 
        setsize = len(numSet)

        if size == setsize: ## This leverages the no duplicates properties of sets
            return False
        return True
