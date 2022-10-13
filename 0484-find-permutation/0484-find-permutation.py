class Solution:
    def findPermutation(self, s: str) -> List[int]:
        ans = [i+1 for i in range(len(s) + 1)]
        dStreak = 0
        for i, ch in enumerate(s):
            if ch == 'I':
                self.reverse(ans, i-dStreak, i)
                dStreak = 0
            else:
                dStreak += 1
                if i == len(s) - 1:
                    self.reverse(ans, i-dStreak+1, i+1)
        return ans
    
    def reverse(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1