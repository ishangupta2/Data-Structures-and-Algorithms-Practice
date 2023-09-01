class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        for s, t, w in times:
            adj[s].append([t, w])
        visit = set()
        minHeap = [[0, k]]
        sz = 0
        while minHeap:
                weight, src = heapq.heappop(minHeap)
                if src in visit:
                    continue
                sz = max(sz, weight)
                visit.add(src)
                for nei, w in adj[src]:
                    if nei not in visit:
                        heapq.heappush(minHeap, [weight + w, nei])
        if len(visit)!=n:
            return -1
        else:
            return sz
        