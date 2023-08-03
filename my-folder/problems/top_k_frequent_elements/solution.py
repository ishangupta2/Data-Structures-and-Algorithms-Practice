class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        heap = []
        arr = []
        for num, freq in d.items():
            heapq.heappush(heap, (-freq, num))
        for i in range(k):
           arr.append(heapq.heappop(heap)[1])
        return arr
                

    