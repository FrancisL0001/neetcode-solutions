class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxV = 0
        while l < r:
            lheight, rheight = heights[l], heights[r]
            h = min(lheight, rheight)
            d = r - l

            maxV = max(maxV, h * d)

            if lheight < rheight:
                l += 1
            else:
                r -= 1

        return maxV
    
    