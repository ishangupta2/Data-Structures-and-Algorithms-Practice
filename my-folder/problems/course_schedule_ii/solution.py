class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            mp[c].append(p)
        output = []
        visit = set()
        trav = set()
        def dfs(crs):
            if crs in trav:
                return False
            if crs in visit:
                return True
            trav.add(crs)
            for p in mp[crs]:
                if not dfs(p):
                    return False
            trav.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output