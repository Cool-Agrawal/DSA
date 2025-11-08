# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = []
        q.append(root)
        s = 0

        while q:
            node = q[0]
            q.pop(0)                
            if node.left and not node.left.left and not node.left.right:
                s += node.left.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)        
        return s
        