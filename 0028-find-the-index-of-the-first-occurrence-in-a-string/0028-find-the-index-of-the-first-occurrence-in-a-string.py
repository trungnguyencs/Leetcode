class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        target = hashcode = 0
        w = len(needle)
        for ch in needle:
            target = target * 26 + self.charToInt(ch)
        for i, ch in enumerate(haystack):
            hashcode = hashcode * 26 + self.charToInt(ch)
            if i >= w:
                hashcode %= 26**w
            if hashcode == target: return i - w + 1
        return -1

    def charToInt(self, ch):
        return ord(ch) - ord('a') + 1