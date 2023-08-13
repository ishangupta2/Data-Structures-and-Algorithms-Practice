# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val
        def helper(node):
            nonlocal maxSum

            if not node:
                return 0
            l, r = helper(node.left), helper(node.right)
            l, r = max(l, 0), max(r, 0)
            maxSum = max(node.val+l+r, maxSum)
            return node.val + max(l,r)
        helper(root)
        return maxSum