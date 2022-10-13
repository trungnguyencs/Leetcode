"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        dic = {node: Node(node.val)}
        q = deque([node])
        while q:
            cur = q.popleft()
            for neigh in cur.neighbors:
                if neigh not in dic:
                    dic[neigh] = Node(neigh.val)
                    q.append(neigh)
                dic[cur].neighbors.append(dic[neigh])
        return dic[node]