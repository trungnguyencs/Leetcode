# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque([root])
        while q:
            total = count = 0
            for _ in range(len(q)):
                cur = q.popleft()
                total += cur.val
                count += 1
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans.append(total/float(count))
        return ans