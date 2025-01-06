class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # similar to 238. Product of Array Except Self and 42. Trapping Rain Water
        # example for leftCost:
        # input     11010
        # leftCount 01223
        # leftCost  01358
        ans = [0]*len(boxes)
        leftCount, leftCost, rightCount, rightCost, n = 0, 0, 0, 0, len(boxes)
        for i in range(1, n):
            if boxes[i-1] == '1': leftCount += 1
            leftCost += leftCount # each step move to right, the cost increases by # of 1s on the left
            ans[i] += leftCost
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1': rightCount += 1
            rightCost += rightCount
            ans[i] += rightCost
        return ans