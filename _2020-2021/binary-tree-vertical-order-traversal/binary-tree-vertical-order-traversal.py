# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        dic = defaultdict(list)
        dic[0].append(root.val)
        q = deque([(root, 0)])
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                cur, offset = q.popleft()
                if cur.left:
                    dic[offset - 1].append(cur.left.val)
                    q.append([cur.left, offset - 1])
                if cur.right:
                    dic[offset + 1].append(cur.right.val)
                    q.append([cur.right, offset + 1])
        return [dic[offset] for offset in range(-level, level + 1) if dic[offset]]