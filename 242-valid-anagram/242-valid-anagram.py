class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter(s)
        for ch in t:
            if ch not in counter: return False
            counter[ch] -= 1
            if counter[ch] == 0: del counter[ch]
        return len(counter) == 0