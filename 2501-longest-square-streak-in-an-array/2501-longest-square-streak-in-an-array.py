class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        numSet = set(nums)
        visited = set()
        maxStreak = -1
        for num in nums:
            if num in visited: continue
            streak = 0
            while num in numSet:
                visited.add(num)
                num = num**2
                streak += 1
            if streak > 1:
                maxStreak = max(maxStreak, streak)
        return maxStreak