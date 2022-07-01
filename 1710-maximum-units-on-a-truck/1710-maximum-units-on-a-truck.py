class Solution:
    def maximumUnits(self, boxes: List[List[int]], capacity: int) -> int:
        boxes.sort(key=lambda x: -x[1])
        ans = 0
        for boxCount, units in boxes:
            if boxCount <= capacity:
                ans += boxCount * units
                capacity -= boxCount
            else:
                ans += capacity * units
                break
        return ans