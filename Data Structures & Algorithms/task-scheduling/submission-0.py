class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()

        maxHeap = [-ct for ct in Counter(tasks).values()]
        heapq.heapify(maxHeap) 

        time = 0

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else: 
                cur = 1 + heapq.heappop(maxHeap)
                if cur:
                    q.append([cur, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
            


