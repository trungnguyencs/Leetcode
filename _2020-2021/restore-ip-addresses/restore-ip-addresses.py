class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = []
        self.backtrack(s, [], 0)
        return self.ans
    
    def backtrack(self, s, arr, i):
        if len(arr) > 4: return
        if i == len(s):
            if len(arr) == 4: self.ans.append('.'.join(map(str, arr)))
            return
        d = int(s[i])
        self.backtrack(s, arr + [d], i+1)
        if arr and arr[-1] != 0 and arr[-1]*10 + d <= 255:
            arr[-1] = arr[-1]*10 + d
            self.backtrack(s, arr, i+1)