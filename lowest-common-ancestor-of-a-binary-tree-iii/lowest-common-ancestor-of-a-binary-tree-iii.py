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
        # O(n) space:
        # pParents = set()
        # while p:
        #     pParents.add(p)
        #     p = p.parent
        # while q not in pParents:
        #     q = q.parent
        # return q
    
        # O(1) space:
        pParent, qParent = p, q
        while pParent != qParent:
            pParent = pParent.parent if pParent.parent else q
            qParent = qParent.parent if qParent.parent else p
        return pParent