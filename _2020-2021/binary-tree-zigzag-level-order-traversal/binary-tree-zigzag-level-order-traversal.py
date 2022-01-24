# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        ans = []
        even = True
        while q:
            level = []
            if even:
                for _ in range(len(q)):
                    cur = q.popleft()
                    level.append(cur.val)
                    if cur.left: q.append(cur.left)
                    if cur.right: q.append(cur.right)
            else:
                for _ in range(len(q)):
                    cur = q.pop()
                    level.append(cur.val)
                    if cur.right: q.appendleft(cur.right)
                    if cur.left: q.appendleft(cur.left)
            ans.append(level)
            even = not even
        return ans    