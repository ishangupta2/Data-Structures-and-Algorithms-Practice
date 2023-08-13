# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        i = k
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            m = stack.pop()
            if i == 1:
                return m.val
            root = m.right
            i-=1
        

           

            
