class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        def volume(left, right):
            return min(heights[left], heights[right]) * (right - left)

        res = volume(0, n - 1)

        l, r = 0, n - 1

        while l < r:
            curVol = volume(l, r)
            if curVol > res:
                res = curVol

                if heights[l] < heights[r]:
                    l += 1
                else:
                    r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
    
    