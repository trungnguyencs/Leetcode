"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # similar to find interestion of 2 linked lists
        curP, curQ = p, q
        while curP != curQ:
            curP = curP.parent if curP else q
            curQ = curQ.parent if curQ else p
        return curP