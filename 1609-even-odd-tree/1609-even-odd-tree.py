# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0
        while q:
            prev = -float('inf') if level % 2 == 0 else float('inf')
            for _ in range(len(q)):
                cur = q.popleft()
                if level % 2 == cur.val % 2: return False
                if level % 2 == 0:
                    if cur.val <= prev: return False
                elif cur.val >= prev: return False
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                prev = cur.val
            level += 1
        return True