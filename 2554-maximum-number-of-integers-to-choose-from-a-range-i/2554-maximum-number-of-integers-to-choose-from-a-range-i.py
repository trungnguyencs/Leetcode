class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        curSum = count = 0
        for num in range(1, n + 1):
            if num in banned: continue
            if curSum + num <= maxSum:
                curSum += num
                count += 1
            else:
                break
        return count