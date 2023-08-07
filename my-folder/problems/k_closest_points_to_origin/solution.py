class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        rtr = []
        for x,y in points:
            dist = (x**2 )+(y**2)
            arr.append((dist, x, y))
        heapq.heapify(arr)
        while k!=0:
          x, y, z = heapq.heappop(arr)
          rtr.append((y, z))
          k-=1
        return rtr
