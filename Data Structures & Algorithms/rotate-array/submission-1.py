class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        
        for i in range(k):
            last = nums[n - 1]

            r = n - 1

            while r > 0:
                nums[r] = nums[r - 1]
                r -= 1

            nums[0] = last


        