class Solution:
    def readBinaryWatch(self, n: int) -> List[str]:
        self.ans = set()
        self.hours = [8, 4, 2, 1]
        self.minutes = [32, 16, 8, 4, 2, 1]
        self.backtrack(0, 0, 0, 0, n)
        return sorted(list(self.ans))

    def backtrack(self, h, m, i, j, n):
        if n == 0:
            h = str(h)
            m = '0' + str(m) if m < 10 else str(m)
            self.ans.add(h + ':' + m)
            return
        if i < 4:
            if h + self.hours[i] < 12:
                self.backtrack(h + self.hours[i], m, i + 1, j, n - 1)  
            self.backtrack(h, m, i + 1, j, n)          
        if j < 6:
            if m + self.minutes[j] < 60:
                self.backtrack(h, m + self.minutes[j], i, j + 1, n - 1)
            self.backtrack(h, m, i, j + 1, n)