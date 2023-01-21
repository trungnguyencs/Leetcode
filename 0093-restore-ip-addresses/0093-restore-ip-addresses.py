class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = []
        self.backtrack(s, 0, [])
        return self.ans
    
    def backtrack(self, s, i, arr):
        if i == len(s):
            if len(arr) == 4:
                self.ans.append('.'.join(arr))
            return
        if len(arr) <= 3:
            self.backtrack(s, i+1, arr + [s[i]])
        if 1 <= len(arr) <= 4 and arr[-1] != '0' and int(arr[-1] + s[i]) <= 255:
            arr[-1] += s[i]
            self.backtrack(s, i+1, arr)