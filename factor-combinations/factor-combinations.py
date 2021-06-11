class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        self.ans = []
        self.factorList = self.getFactorList(n)
        self.backtrack([], 0, n)
        return self.ans
        
    def backtrack(self, arr, i, n):
        if n == 1:
            if arr: self.ans.append(arr[:])
            return
        for j in range(i, len(self.factorList)):
            num = self.factorList[j]
            if num > n: return
            if n % num == 0:
                self.backtrack(arr + [num], j, n//num)
            
    def getFactorList(self, n):
        return [i for i in range(2, n//2 + 1) if n % i == 0]