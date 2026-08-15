import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        window = [-nums[0]]
        heapq.heapify(window)
        cur = {}
        cur[nums[0]] = 1
        res = []
        l = 0
        for r in range(1, len(nums)):
            heapq.heappush(window, -nums[r])
            cur[nums[r]] = cur.get(nums[r], 0) + 1
            if r >= k - 1:
                if r - l + 1 > k: 
                    cur[nums[l]] -= 1
                    l += 1

                while cur.get(-window[0], 0) == 0:
                    heapq.heappop(window)

                res.append(-window[0])

        return res

