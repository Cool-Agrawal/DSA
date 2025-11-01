"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        a = []
        self.hei(root,a)
        return a
    def hei(self,root,a):
        if root is None:
            return 
        for i in root.children:
            self.hei(i,a)
        a.append(root.val)
    
        