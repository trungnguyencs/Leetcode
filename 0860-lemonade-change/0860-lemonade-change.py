class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveCount = tenCount = 0
        for b in bills:
            if b == 5:
                fiveCount += 1
            elif b == 10:
                if fiveCount == 0: return False
                fiveCount -= 1
                tenCount += 1
            elif b == 20:
                if tenCount >= 1 and fiveCount >= 1:
                    tenCount -= 1
                    fiveCount -= 1
                elif fiveCount >= 3:
                    fiveCount -= 3
                else:
                    return False
        return True