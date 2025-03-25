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
        # #O(n) space:
        # seen = set([p, q])
        # while p or q:
        #     if p:
        #         p = p.parent
        #         if p in seen: return p
        #         seen.add(p)
        #     if q:
        #         q = q.parent
        #         if q in seen: return q
        #         seen.add(q)
        # O(1) space: similar to 160. Intersection of Two Linked Lists
        pParent, qParent = p, q
        while pParent != qParent:
            pParent = pParent.parent if pParent.parent else q
            qParent = qParent.parent if qParent.parent else p
        return pParent