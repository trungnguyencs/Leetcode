class Solution:
    def isSubsequence(self, short: str, long: str) -> bool:
        if not short: return True
        i = 0
        for ch in long:
            if ch == short[i]:
                i += 1
                if i == len(short): return True
        return False