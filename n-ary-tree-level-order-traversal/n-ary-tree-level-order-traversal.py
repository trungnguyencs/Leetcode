"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        ans = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                level.append(cur.val)
                q.extend(cur.children)
            ans.append(level)
        return ans