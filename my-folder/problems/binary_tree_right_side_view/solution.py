# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        stk = []

        if root:
            queue.append(root)
        while len(queue)>0:
            for i in range(len(queue)):
                a = queue.popleft()
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
            stk.append(a.val)
        return stk