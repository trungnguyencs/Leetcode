# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        G = defaultdict(list)
        self.buildGraph(root, G)
        return self.bfs(G, target, k)
        
    def buildGraph(self, root, G):
        if not root: return
        if root.left:
            G[root].append(root.left)
            G[root.left].append(root)
            self.buildGraph(root.left, G)
        if root.right:
            G[root].append(root.right)
            G[root.right].append(root)
            self.buildGraph(root.right, G)
            
    def bfs(self, G, target, k):
        q = deque([target])
        visited = {target}
        for _ in range(k):
            for _ in range(len(q)):
                cur = q.popleft()
                for neigh in G[cur]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append(neigh)
        return [node.val for node in q]