class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()
        minHeights = [warehouse[0]]*len(warehouse)
        for i in range(1, len(warehouse)):
            minHeights[i] = min(minHeights[i-1], warehouse[i])
        j = 0
        for minHeight in reversed(minHeights):
            if boxes[j] <= minHeight:
                j += 1
            if j == len(boxes): break    
        return j