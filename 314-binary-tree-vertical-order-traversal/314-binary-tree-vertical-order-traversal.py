# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        dic = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            cur, offset = q.popleft()
            dic[offset].append(cur.val)
            if cur.left:
                q.append((cur.left, offset - 1))
            if cur.right:
                q.append((cur.right, offset + 1))
        return [dic[offset] for offset in sorted(dic.keys())]