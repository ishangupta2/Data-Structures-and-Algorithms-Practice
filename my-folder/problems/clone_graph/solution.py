"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mp = {}
        def dfs(node):
            if not node:
                return 
            if node in mp:
                return mp[node]
            else:
                copy = Node(node.val)
                mp[node] = copy
                for n in node.neighbors:
                    copy.neighbors.append(dfs(n))
                return copy
        return dfs(node)