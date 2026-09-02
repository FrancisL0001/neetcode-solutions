class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        turtle, hare = 0, 0
        while True:
            turtle = nums[turtle]
            hare = nums[nums[hare]]
            if turtle == hare:
                break

        turtle2 = 0
        while True:
            turtle = nums[turtle]
            turtle2 = nums[turtle2]
            if turtle == turtle2:
                return turtle

        