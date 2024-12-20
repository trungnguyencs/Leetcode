# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0
        while q:
            level += 1
            nextQ = []
            while q:
                cur = q.popleft()
                if cur.left:
                    nextQ.extend([cur.left, cur.right])
            if level % 2 == 1:
                self.reverse(nextQ)
            q = deque(nextQ)
        return root
    
    def reverse(self, q):
        i, j = 0, len(q) - 1
        while i < j:
            q[i].val, q[j].val = q[j].val, q[i].val
            i += 1
            j -= 1