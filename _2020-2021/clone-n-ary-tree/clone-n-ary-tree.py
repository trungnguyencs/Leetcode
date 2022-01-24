"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root: return None
        dic = {root: Node(root.val)}
        q = deque([root])
        while q:
            cur = q.popleft()
            for child in cur.children:
                dic[child] = Node(child.val)
                dic[cur].children.append(dic[child])
                q.append(child)
        return dic[root]