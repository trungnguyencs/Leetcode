class Solution:
    def letterCombinations(self, s: str) -> List[str]:
        if not s:
            return []
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        self.ans = []
        self.backtrack(s, 0, [], dic)
        return self.ans
        
    def backtrack(self, s, i, arr, dic):
        if i == len(s):
            self.ans.append(''.join(arr))
            return
        for ch in dic[s[i]]:
            arr.append(ch)
            self.backtrack(s, i + 1, arr, dic)
            arr.pop() 