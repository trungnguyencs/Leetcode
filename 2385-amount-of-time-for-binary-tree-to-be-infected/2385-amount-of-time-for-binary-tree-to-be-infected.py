# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        G = defaultdict(list)
        self.buildGraph(root, G)
        return self.bfs(start, G)
        
    def buildGraph(self, root, G):
        if root.left:
            G[root.val].append(root.left.val)
            G[root.left.val].append(root.val)
            self.buildGraph(root.left, G)
        if root.right:
            G[root.val].append(root.right.val)
            G[root.right.val].append(root.val)
            self.buildGraph(root.right, G)
            
    def bfs(self, start, G):
        q = deque([start])
        visited = {start: 0}
        while q:
            cur = q.popleft()
            for neigh in G[cur]:
                if neigh not in visited:
                    visited[neigh] = visited[cur] + 1
                    q.append(neigh)
        return visited[cur]      