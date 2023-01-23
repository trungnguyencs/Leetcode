class Solution:
    def confusingNumberII(self, n: int) -> int:
        dic = {0:0, 1:1, 6:9, 8:8, 9:6}
        self.ans = 0
        self.backtrack(0, dic, n)
        return self.ans
    
    def backtrack(self, num, dic, n):
        if num > n: return
        if num != 0 and num != self.flip(num, dic):
            self.ans += 1
        for d in dic:
            if num == 0 and d == 0: continue
            self.backtrack(num*10 + d, dic, n)
    
    def flip(self, num, dic):
        flippedNum = 0
        while num > 0:
            flippedNum = flippedNum * 10 + dic[num % 10]
            num //= 10
        return flippedNum