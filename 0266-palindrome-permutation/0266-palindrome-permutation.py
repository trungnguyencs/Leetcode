class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        return sum(freq % 2 == 1 for freq in counter.values()) <= 1