class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        s, x = str(N), 1
        counter_s = Counter(s)
        while x < 10**(len(s)+1):
            if len(str(x)) == len(s) and Counter(str(x)) == counter_s: return True
            x *= 2
        return False