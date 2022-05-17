# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = deque([(original, cloned)])
        while q:
            cur, curCopy = q.popleft()
            if cur is target: return curCopy
            if cur.left:
                q.append((cur.left, curCopy.left))
            if cur.right:
                q.append((cur.right, curCopy.right))