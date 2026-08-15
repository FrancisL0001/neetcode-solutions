class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, min(1, len(nums) - 1)
        minL = len(nums) + 1

        if l == r:
            return 1 if target <= nums[0] else 0

        running = nums[l]

        while r <= len(nums) and l < r:
            if running >= target:
                minL = min(minL, r - l)
                running -= nums[l]
                l += 1
            else:
                running += nums[r] if r < len(nums) else 0
                r += 1

        return minL if minL < len(nums) + 1 else 0