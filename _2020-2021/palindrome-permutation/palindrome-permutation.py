class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        oddFound = False
        for v in counter.values():
            if v % 2 == 1:
                if oddFound: return False
                oddFound = True
        return True