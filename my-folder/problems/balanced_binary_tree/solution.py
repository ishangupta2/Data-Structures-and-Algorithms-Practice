# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bal(node):
            if not node:
                return 0
            else:
                l, r = bal(node.left), bal(node.right)
                if l==-1 or r==-1:
                    return -1
                if abs(l-r)>1:
                    return -1
                return 1+max(l,r)
        return bal(root)>=0
