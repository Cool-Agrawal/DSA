# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        m = float("inf")
        self.inorder(root, res)
        for i in range(1, len(res)):
            m = min(m, res[i] - res[i - 1])
        return m

    def inorder(self, root, res):
        if root is None:
            return 0
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)
        return res
