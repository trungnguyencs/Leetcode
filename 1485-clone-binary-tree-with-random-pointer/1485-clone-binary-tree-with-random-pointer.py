# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root: return None
        dic = {root: NodeCopy(root.val)}
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur.left:
                if cur.left not in dic:
                    dic[cur.left] = NodeCopy(cur.left.val)
                dic[cur].left = dic[cur.left]
                q.append(cur.left)
            if cur.right:
                if cur.right not in dic:
                    dic[cur.right] = NodeCopy(cur.right.val)
                dic[cur].right = dic[cur.right]
                q.append(cur.right)
            if cur.random:
                if cur.random not in dic:
                    dic[cur.random] = NodeCopy(cur.random.val)
                dic[cur].random = dic[cur.random]
        return dic[root]                