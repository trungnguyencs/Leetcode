class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = streak = 0
        firstStreak = True
        for num in seats:
            if num == 0:
                streak += 1
            else:
                ans = max(ans, streak) if firstStreak else max(ans, (streak + 1)//2)
                firstStreak = False
                streak = 0
        ans = max(ans, streak)
        return ans