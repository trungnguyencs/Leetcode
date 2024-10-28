class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # # O(nlogn)
        # nums.sort()
        # numSet = set(nums)
        # visited = set()
        # maxStreak = -1
        # for num in nums:
        #     if num in visited: continue
        #     streak = 0
        #     while num in numSet:
        #         visited.add(num)
        #         num = num**2
        #         streak += 1
        #     if streak > 1:
        #         maxStreak = max(maxStreak, streak)
        # return maxStreak
        
        # O(n): similar to 128. Longest Consecutive Sequence
        numSet = set(nums)
        visited = set()
        maxStreak = -1
        for num in nums:
            sqrt = int(num**0.5)
            if sqrt in numSet and sqrt**2 == num:
                continue
            streak = 0
            while num in numSet:
                num = num**2
                streak += 1
            maxStreak = max(maxStreak, streak)
        return -1 if maxStreak == 1 else maxStreak