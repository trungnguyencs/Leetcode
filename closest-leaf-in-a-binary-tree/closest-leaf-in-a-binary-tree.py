# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        if root.val == k and not root.left and not root.right: return k
        G = self.buildGraph(root, defaultdict(set))
        q = deque([k])
        visited = set([k])
        while q:
            cur = q.popleft()
            if len(G[cur]) == 1 and cur != root.val: #if leaf
                return cur
            for neigh in G[cur]:
                if neigh in visited: continue
                q.append(neigh)
                visited.add(neigh)
            
    def buildGraph(self, root, dic):
        if not root: return
        if root.left:
            dic[root.val].add(root.left.val)
            dic[root.left.val].add(root.val)
            self.buildGraph(root.left, dic)
        if root.right:
            dic[root.val].add(root.right.val)
            dic[root.right.val].add(root.val)
            self.buildGraph(root.right, dic)
        return dic