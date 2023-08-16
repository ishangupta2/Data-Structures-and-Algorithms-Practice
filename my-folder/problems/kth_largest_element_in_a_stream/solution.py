class KthLargest:
    def __init__(self, k: int, nums: List[int]):        
        self.min, self.k = nums, k
        heapq.heapify(self.min)
        while(len(nums) > k):
            heapq.heappop(self.min)

    def add(self, val: int) -> int:
        heapq.heappush(self.min, val)
        if len(self.min)> self.k:
            heapq.heappop(self.min)
        return self.min[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)