# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], start: int, end: int) -> str:
        G = self.buildGraph(root, defaultdict(list))
        q = deque([(start, '')])
        visited = set([start])
        while q:
            cur, path = q.popleft()
            if cur == end: return path
            for neigh, d in G[cur]:
                if neigh in visited: continue
                q.append((neigh, path + d))
                visited.add(neigh)
        
    def buildGraph(self, root, dic):
        if not root: return
        if root.left:
            dic[root.val].append((root.left.val, 'L'))
            dic[root.left.val].append((root.val, 'U'))
            self.buildGraph(root.left, dic)
        if root.right:
            dic[root.val].append((root.right.val, 'R'))
            dic[root.right.val].append((root.val, 'U'))
            self.buildGraph(root.right, dic)
        return dic