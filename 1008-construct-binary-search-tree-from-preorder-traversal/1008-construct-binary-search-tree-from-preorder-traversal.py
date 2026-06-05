# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        inorder = sorted(preorder)

        def build(preorder,inorder):
            if not preorder or not inorder:
                return None
            root_val = preorder.pop(0)
            root = TreeNode(root_val)
            idx = inorder.index(root_val)
            root.left = build(preorder,inorder[:idx])
            root.right = build(preorder,inorder[idx+1:])
            return root

        return build(preorder,inorder)
        