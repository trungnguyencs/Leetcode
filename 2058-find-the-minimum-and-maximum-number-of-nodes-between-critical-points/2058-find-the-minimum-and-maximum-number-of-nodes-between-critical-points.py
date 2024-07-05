# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first, last, minDistance, i, count = -math.inf, -math.inf, math.inf, 1, 0
        while head and head.next and head.next.next:
            prev, cur, nxt = head.val, head.next.val, head.next.next.val
            if (cur > prev and cur > nxt) or (cur < prev and cur < nxt):
                if first == float('-inf'):
                    first = i
                else:
                    minDistance = min(minDistance, i - last)
                last = i
                count += 1
            head = head.next
            i += 1
        return [-1, -1] if count == 0 or count == 1 else [minDistance, last - first] 