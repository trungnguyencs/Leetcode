"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.ans = 0
        self.postOrder(root)
        return self.ans
    
    def postOrder(self, root):
        if not root: return 0
        M = secondM = 0
        for child in root.children:
            length = self.postOrder(child)
            if length >= M:
                secondM, M = M, length
            elif length > secondM:
                secondM = length
        self.ans = max(self.ans, M + secondM)
        return 1 + M