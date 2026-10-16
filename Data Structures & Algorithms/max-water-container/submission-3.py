class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxV = 0
        while l < r:
            h = min(heights[l], heights[r])
            d = r - l

            maxV = max(maxV, h * d)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxV
    
    