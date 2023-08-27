class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-1*c for c in count.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0
        while(heap or queue):
            time += 1
            if heap:
                cnt = heapq.heappop(heap)+1
                if cnt:
                    queue.append((cnt, time+n))
            if queue and queue[0][1] == time:
                r, c = queue.popleft()
                heapq.heappush(heap, r)
        return time
