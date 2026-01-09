# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        q = [root]
        parent = {root : None}
        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                level.append(node)
                if node.left:
                    parent[node.left] = node
                    q.append(node.left)
                if node.right:
                    parent[node.right] = node
                    q.append(node.right)
        res = set(level)
        while len(res) > 1:
            res = {parent[node] for node in res}
        return list(res)[0]
        