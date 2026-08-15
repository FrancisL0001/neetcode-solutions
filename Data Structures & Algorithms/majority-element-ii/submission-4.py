class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = candidate2 = None
        count1 = count2 = 0
        n = len(nums)

        # Get the candidates
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Verify if they satisfy majority rule
        count1 = nums.count(candidate1)
        count2 = nums.count(candidate2)
        res = []

        if count1 > (n / 3):
            res.append(candidate1)

        if candidate2 != candidate1 and count2 > (n/3):
            res.append(candidate2)

        return res