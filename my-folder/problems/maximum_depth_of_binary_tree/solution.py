# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxx = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
         if not root:
             return 0
         self.maxi(root, 1)
         return self.maxx
    def maxi(self, root, num):
        if not root:
            return 
        else:
            self.maxx = max(self.maxx, num)
            self.maxi(root.right, num+1)
            self.maxi(root.left, num+1)
