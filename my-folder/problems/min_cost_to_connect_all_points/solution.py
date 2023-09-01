class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = []
        xC, yC = points[0]
        for i in range(1, len(points)):
            x, y = points[i]
            dist = abs(xC-x)+abs(yC-y)
            heapq.heappush(minHeap, (dist, 0, i))
        sz = 0
        visit = set()
        visit.add(0)
        while minHeap:
            weight, src, dest = heapq.heappop(minHeap)
            if dest in visit:
                continue
            sz += weight
            visit.add(dest)
            xc, yc = points[dest]
            for i in range(0, len(points)):
                if i not in visit:
                    x, y = points[i]
                    dist = abs(xc-x)+abs(yc-y)
                    heapq.heappush(minHeap, (dist, dest, i))
        return sz

            
            
           
        