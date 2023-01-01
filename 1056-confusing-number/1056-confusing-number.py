class Solution:
    def confusingNumber(self, n: int) -> bool:
        s = str(n)
        dic = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        if any(ch not in dic for ch in s): return False
        return not all(c2 == dic[c1] for c1, c2 in zip(s, reversed(s)))