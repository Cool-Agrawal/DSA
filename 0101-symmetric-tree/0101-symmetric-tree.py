# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sym(self,root1,root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None: return False
        return (root1.val == root2.val) and self.sym(root1.left, root2.right) and self.sym(root1.right, root2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.sym(root.left,root.right)

    
        