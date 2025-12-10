# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return 0
        q = [root]
        res = []
        a = []
        while q:
            level = []
            for i in range(len(q)):
                node = q[0]
                q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        for i in res:
            print(i)
            if len(i) == 1:
                a.append(i[0])
            else:
                a.append(sum(i)/len(i))
        return a
        