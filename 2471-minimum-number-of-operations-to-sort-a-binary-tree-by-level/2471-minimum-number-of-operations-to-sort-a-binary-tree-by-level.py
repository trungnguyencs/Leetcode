# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = 0
        while q:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans += self.countOps(level)
        return ans
    
    def countOps(self, arr):
        dic = {num: i for i, num in enumerate(arr)}
        ops = 0
        for i, (num, target) in enumerate(zip(arr, sorted(arr))):
            if num == target: continue
            i, j = dic[num], dic[target]
            dic[num], dic[target] = j, i
            arr[i], arr[j] = arr[j], arr[i]
            ops += 1
        return ops