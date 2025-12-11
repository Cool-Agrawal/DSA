# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = [root]
        res = []
        m = float('inf')
        while q:
            for i in range(len(q)):
                node = q[0]
                q.pop(0)
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        res = sorted(res)
        for i in range(1,len(res)):
            m = min(m,abs(res[i] - res[i-1]))
        return m
        
        