class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        return self.helper(n, visited)
        
    def helper(self, n, visited):
        if n == 1: return True
        if n in visited: return False
        visited.add(n)
        return self.helper(self.sumSquareDigits(n), visited)
    
    def sumSquareDigits(self, n):
        return sum([int(ch)**2 for ch in str(n)])
        
        
        
            