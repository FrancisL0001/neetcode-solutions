class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        
        here we go with the reasoning that:
        res[i] = prod(nums[0] -> nums[i-1]) * prod(nums[i+1]->nums[last])
        with: 
            res[0] = prod(nums[1] -> nums[last]); 
            res[last] = prod(nums[0] -> nums[last-1])
        
        '''
        
        res = [0] * len(nums) # Initialize the result array as an array size len(nums) of zeros
        asc = list(nums) # array of products of numbers where: asc[i] = prod(nums[0] -> nums[i])
        desc = list(nums) # array of products of numbers where: desc[i] = prod(nums[i] -> nums[last])

        last = len(nums) - 1

        for i in range(1, len(nums)):
            asc[i] = asc[i-1] * asc[i] # asc[i] = prod(nums[0] -> nums[i])
            desc[last - i] = desc[last - i + 1] * desc[last - i] # desc[i] = prod(nums[i] -> nums[last])

        res[0] = desc[1]
        for i in range(1, len(nums) - 1):
            res[i] = asc[i-1] * desc[i+1] 
        res[last] = asc[last-1]
        return res