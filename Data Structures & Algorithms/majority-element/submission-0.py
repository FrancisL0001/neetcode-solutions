class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        maj = (len(nums) / 2)
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1

            if count[num]>maj:
                return num 