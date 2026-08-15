import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        window = [(-nums[0], 0)]
        heapq.heapify(window)
        res = []
        l = 0

        for r in range(1, len(nums)):
            heapq.heappush(window, (-nums[r], r))
            if r >= k - 1:
                if r - l + 1 > k: 
                    l += 1

                while window[0][1] < l:
                    heapq.heappop(window)

                res.append(-window[0][0])

        return res

