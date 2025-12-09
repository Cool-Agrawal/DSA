# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        self.inorder(root,res)
        x = y = None
        for i in range(1,len(res)):
            if res[i].val < res[i-1].val:
                if not x:
                    x = res[i-1]
                    y = res[i]
                else:
                    y = res[i]
        x.val,y.val = y.val,x.val
        return root
        
    def inorder(self,root,res):
        if not root:
                return None
        self.inorder(root.left,res)
        res.append(root)
        self.inorder(root.right,res)
        return res
        