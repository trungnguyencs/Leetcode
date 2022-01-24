class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        prev = self.countAndSay(n-1) + '#'
        cur = []
        count = 1
        for i in range(len(prev)-1):
            if prev[i] == prev[i+1]:
                count += 1
            else:
                cur.extend([str(count), prev[i]])
                count = 1
        return ''.join(cur)
