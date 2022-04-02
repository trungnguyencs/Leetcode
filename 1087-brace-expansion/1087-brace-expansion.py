class Solution:
    def expand(self, s: str) -> List[str]:
        s = s.replace('{', ' ').replace('}', ' ').split()
        self.ans = []
        self.backtrack(s, 0, [])
        # return sorted(self.ans) # optimization
        return self.ans
               
    def backtrack(self, s, i, arr):
        if i == len(s):
            self.ans.append(''.join(arr))
            return
        if len(s[i]) == 1:
            self.backtrack(s, i+1, arr + [s[i]])
        else:
            # for ch in s[i].split(','):
            for ch in sorted(s[i].split(',')): # optimization
                self.backtrack(s, i+1, arr + [ch])