class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set([n])
        while True:
            tmp = 0
            while n != 0:
                tmp += (n % 10)**2
                n //= 10
            if tmp == 1: return True
            if tmp in visited: return False
            visited.add(tmp)
            n = tmp     