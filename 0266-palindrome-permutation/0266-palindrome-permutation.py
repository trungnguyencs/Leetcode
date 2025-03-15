class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        return len([ch for ch, freq in counter.items() if freq % 2 == 1]) <= 1