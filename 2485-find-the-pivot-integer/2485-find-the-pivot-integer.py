class Solution:
    def pivotInteger(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi)//2
            leftSum = self.consecutiveSum(1, mid)
            rightSum = self.consecutiveSum(mid, n)
            if leftSum == rightSum: return mid
            if leftSum < rightSum:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
    
    def consecutiveSum(self, start, end):
        return end*(end + 1)//2 - (start - 1)*start//2