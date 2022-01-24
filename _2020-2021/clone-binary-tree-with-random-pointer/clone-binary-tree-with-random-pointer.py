# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root: return None
        visited = {root: NodeCopy(root.val)}
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur.left:
                if cur.left not in visited:
                    visited[cur.left] = NodeCopy(cur.left.val)
                visited[cur].left = visited[cur.left]
                q.append(cur.left)
            if cur.right:
                if cur.right not in visited:
                    visited[cur.right] = NodeCopy(cur.right.val)
                visited[cur].right = visited[cur.right]
                q.append(cur.right)
            if cur.random:
                if cur.random not in visited:
                    visited[cur.random] = NodeCopy(cur.random.val)
                visited[cur].random = visited[cur.random]
        return visited[root]            