class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        con = [1]*(len(edges)+1)
        def find(n):
            p = par[n]
            while p!=par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        def union(n1, n2):
            n1, n2 = find(n1), find(n2)
            if n1 == n2:
                return False
            if con[n1]>con[n2]:
                par[n2] = n1
                con[n1]+=con[n2]
            else:
                par[n1] = n2
                con[n2]+=con[n1]
            return True
        for n1, n2 in edges:
           if not union(n1, n2):
               return [n1, n2]
