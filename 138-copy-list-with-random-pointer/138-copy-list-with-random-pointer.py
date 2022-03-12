"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        dic = {head: Node(head.val)}
        cur = head
        while cur:
            if cur.next:
                if cur.next not in dic:
                    dic[cur.next] = Node(cur.next.val)
                dic[cur].next = dic[cur.next]
            if cur.random:
                if cur.random not in dic:
                    dic[cur.random] = Node(cur.random.val)
                dic[cur].random = dic[cur.random]
            cur = cur.next
        return dic[head]