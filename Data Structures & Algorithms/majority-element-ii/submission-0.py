class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elts = {}

        for num in nums:
            if num in elts:
                elts[num] += 1
            else:
                elts[num] = 1

        res = []
        n = len(nums)
        for elt, freq in elts.items():
            if elts[elt] > (n / 3):
                res.append(elt)
        
        return res