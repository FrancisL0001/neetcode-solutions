class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        heapq.heapify(maxHeap)

        for stone in stones:
            heapq.heappush(maxHeap, -1 * stone)

        while len(maxHeap) > 1:
            top = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)

            if top < second:
                heapq.heappush(maxHeap, top - second)

        if maxHeap:
            return -1 * maxHeap[0]

        return 0

