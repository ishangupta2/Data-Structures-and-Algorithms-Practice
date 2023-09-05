class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i in range(len(intervals)):
            if not res or res[-1][1] < intervals[i][0]:
                    res.append(intervals[i])
            else:
                temp = res[-1]
                res[-1] = [min(temp[0], intervals[i][0]), max(temp[1], intervals[i][1])]
        return res
        