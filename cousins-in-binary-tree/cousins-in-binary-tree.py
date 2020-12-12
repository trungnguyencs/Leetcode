# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        firstParent = None
        q = collections.deque([(root, None)])
        while q:
            for _ in range(len(q)):
                cur, parent = q.popleft()
                if cur.val in [x, y]:
                    if not firstParent:
                        firstParent = parent
                    else:
                        return parent != firstParent
                if cur.left:
                    q.append((cur.left, cur))
                if cur.right:
                    q.append((cur.right, cur))
            if firstParent: return False
                        
