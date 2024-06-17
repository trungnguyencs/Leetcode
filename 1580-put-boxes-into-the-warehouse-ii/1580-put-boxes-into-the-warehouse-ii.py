class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # Greedy solution: fit biggest boxes from both ends first
        i, j = 0, len(warehouse) - 1
        ans = 0
        for b in sorted(boxes, reverse=True):
            if i > j: break
            if b <= warehouse[i]:
                i += 1
                ans += 1
            elif b <= warehouse[j]:
                j -= 1
                ans += 1
        return ans