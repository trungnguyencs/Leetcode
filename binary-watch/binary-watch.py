class Solution:
    def readBinaryWatch(self, bits: int) -> List[str]:
        self.nums = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        self.ans = []
        self.backtrack(0, 0, 0, bits)
        return self.ans[::-1]
    
    def backtrack(self, i, hours, minutes, bits):
        if not bits:
            if (hours, minutes) == (12, 0): return "12:00"
            if hours >= 12 or minutes >= 60: return
            self.ans.append("{}:{:02d}".format(hours, minutes))
            return
        if i == len(self.nums): return
        for j in range(i, len(self.nums)):
            if 0 <= j <= 3:
                self.backtrack(j+1, hours+self.nums[j], minutes, bits - 1)
            else:
                self.backtrack(j+1, hours, minutes+self.nums[j], bits - 1)
        