class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        l, r = 0, min(1, n - 1)
        minL = n + 1

        if l == r:
            return 1 if target <= nums[0] else 0

        running = nums[l]

        while r <= n and l < r:
            if running >= target:
                minL = min(minL, r - l)
                running -= nums[l]
                l += 1
            else:
                running += nums[r] if r < n else 0
                r += 1

        return minL if minL < n + 1 else 0