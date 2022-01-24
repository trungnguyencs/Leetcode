class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(ransomNote)
        for ch in magazine:
            if ch not in counter: continue
            counter[ch] -= 1
            if counter[ch] == 0:
                del counter[ch]
                if not counter: break
        return not counter