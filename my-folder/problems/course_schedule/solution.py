class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
           mp[c].append(p)
        def dfs(pre, visit):
            if pre in visit:
                return False
            if mp[pre] == []:
                return True
            visit.add(pre)
            for l in mp[pre]:
                if not dfs(l, visit):
                    return False
            visit.remove(pre)
            mp[pre] = []
            return True
        for c in range(numCourses):
            if not dfs(c, set()):
                return False
        return True