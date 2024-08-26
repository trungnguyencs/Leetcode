"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.ans = []
        self.dfs(root)
        return self.ans
        
    def dfs(self, root):
        if not root: return
        for node in root.children:
            self.dfs(node)
        self.ans.append(root.val)