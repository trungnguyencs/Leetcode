class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # Greedy solution: fit biggest boxes from both ends first
        i, j = 0, len(warehouse) - 1
        minLeft, minRight = warehouse[0], warehouse[-1]
        boxes.sort()
        ans = 0
        while i <= j:
            if not boxes: break
            b = boxes.pop()
            if b <= minLeft:
                i += 1
                ans += 1
                if i < len(warehouse): minLeft = min(minLeft, warehouse[i])
            elif b <= warehouse[j]:
                j -= 1
                ans += 1
                if j >= 0: minRight = min(minRight, warehouse[j])
        return ans