# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        c = 0
        def dfs(node):
            nonlocal c
            if not node:
                return []
            a = dfs(node.left)
            b = dfs(node.right)
            ans = a + b + [node.val]
            if sum(ans)//len(ans) == node.val:
                c += 1
            return ans
        dfs(root)
        return c
        