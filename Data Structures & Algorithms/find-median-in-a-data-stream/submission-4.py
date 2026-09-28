class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.n = 0
        self.maxHeap = []

        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        # maxheap store the n/2 smallest and minheap store the n/2 highest
        if not self.maxHeap:
            heapq.heappush(self.maxHeap, -1*num)
        elif not self.minHeap:
            if num < -1 * self.maxHeap[0]:
                cur = -1 * heapq.heappop(self.maxHeap)
                heapq.heappush(self.maxHeap, -1 * num)
                heapq.heappush(self.minHeap, cur)
            else:
                heapq.heappush(self.minHeap, num) 
        elif num > self.minHeap[0]:
            if len(self.maxHeap) > len(self.minHeap):
                heapq.heappush(self.minHeap, num) 
            else:
                heapq.heappush(self.minHeap, num) 
                cur = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -1*cur)
        else:
            heapq.heappush(self.maxHeap, -1*num)
            if len(self.maxHeap) > len(self.minHeap) + 1:
                cur = -1 * heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, cur) 
        
        self.n += 1   

    def findMedian(self) -> float:  
        if self.n % 2 == 0:
            return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2

        return -1 * self.maxHeap[0]
        
        