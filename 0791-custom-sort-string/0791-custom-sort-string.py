class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = {ch: i for i, ch in enumerate(order)}
        s = list(s)
        s.sort(key=lambda ch: dic[ch] if ch in dic else 0)
        return ''.join(s)