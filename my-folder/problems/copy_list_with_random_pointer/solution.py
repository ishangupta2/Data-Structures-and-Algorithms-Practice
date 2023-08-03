"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        mp = {None: None}
        while (cur):
            mp[cur] = Node(cur.val, None, None)
            cur = cur.next
        for k, v in mp.items():
            if k == None:
                continue
            v.next = mp[k.next]
            v.random = mp[k.random]
        return mp[head]
        

