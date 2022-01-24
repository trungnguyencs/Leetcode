class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter, orderSet, charSet = Counter(s), set(order), set(s)
        return ''.join([ch*counter[ch] for ch in order] + [ch*counter[ch] for ch in charSet if ch not in orderSet])