class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i], warehouse[i-1])
        boxes.sort()
        j = 0
        for height in reversed(warehouse):
            if height >= boxes[j]:
                j += 1
            if j == len(boxes): break
        return j