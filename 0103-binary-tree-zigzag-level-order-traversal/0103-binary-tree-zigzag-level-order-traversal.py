# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = []
        res = []
        q.append(root)
        count = 1
        while q:
            n = len(q)
            level  = []
            for i in range(n):
                node = q[0]
                q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if count % 2 == 0:
                level.reverse()
            res.append(level)
            count += 1
        return res

        