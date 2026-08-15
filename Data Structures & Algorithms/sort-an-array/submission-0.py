class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(set(nums)) <= 1:
            return nums

        med = len(nums) // 2

        if len(nums) == 2 and nums[0] <= nums[1]:
            return nums
        else:
            left = [r for r in nums if r < nums[med]]
            right = [r for r in nums if r > nums[med]]
            pivot = [r for r in nums if r == nums[med]]
            return self.sortArray(left) + pivot + self.sortArray(right)
            