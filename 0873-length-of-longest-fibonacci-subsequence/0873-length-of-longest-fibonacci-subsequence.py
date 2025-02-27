class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        numSet = set(arr)
        maxStreak = 2
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                a, b, streak = arr[i], arr[j], 2
                while a + b in numSet:
                    a, b, streak = b, a + b, streak + 1
                maxStreak = max(maxStreak, streak)
        return 0 if maxStreak == 2 else maxStreak