# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        cur = dummy = PolyNode()
        while poly1 or poly2:
            if not poly2 or (poly1 and poly1.power > poly2.power):
                cur.next = PolyNode(poly1.coefficient, poly1.power)
                poly1 = poly1.next
                cur = cur.next
            elif not poly1 or (poly2 and poly2.power > poly1.power):
                cur.next = PolyNode(poly2.coefficient, poly2.power)
                poly2 = poly2.next
                cur = cur.next
            else: # poly1 and poly2 and poly1.power == poly2.power
                if poly1.coefficient + poly2.coefficient != 0:
                    cur.next = PolyNode(poly1.coefficient + poly2.coefficient, poly1.power)
                    cur = cur.next
                poly1 = poly1.next
                poly2 = poly2.next
        return dummy.next if dummy.next else []