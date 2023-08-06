class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if(len(stones) == 1):
            return stones[0]
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while(len(stones)> 1):
            f = heapq.heappop(stones)
            j = heapq.heappop(stones)
            if(f != j):
                heapq.heappush(stones, f-j)
        
        return abs(stones[0]) if stones else 0