class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.backtrack([], 0, 0, 2*n)
        return self.ans
    
    def backtrack(self, arr, open, close, n):
        if n == 0:
            if open == close:
                self.ans.append(''.join(arr))
            return
        arr.append('(')
        self.backtrack(arr, open + 1, close, n-1)
        arr.pop()
        if open > close:
            arr.append(')')
            self.backtrack(arr, open, close + 1, n-1)
            arr.pop()
            