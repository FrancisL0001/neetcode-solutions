class Solution: 
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)

        for point in points:
            dis = point[0] ** 2 + point[1] ** 2

            cur = (-1 * dis, point)

            heapq.heappush(minHeap, cur)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return [point for dis, point in minHeap]