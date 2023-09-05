class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        prevend = intervals[0][1]
        for start, end in intervals[1:]:
           if start >= prevend:
               prevend = end
           else:
                res+=1
                prevend = min(end, prevend)
        return res

        