class Solution:
    def distanceToOrigin(self, point):
        return (point[0] ** 2 + point[1] ** 2) ** 0.5

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)

        for point in points:
            dis = self.distanceToOrigin(point)

            cur = (-1 * dis, point)

            heapq.heappush(minHeap, cur)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return [point for dis, point in minHeap]