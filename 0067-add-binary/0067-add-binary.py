class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry:
            d1 = int(a[i]) if i >= 0 else 0
            d2 = int(b[j]) if j >= 0 else 0
            carry, d = divmod(d1 + d2 + carry, 2)
            ans.append(str(d))
            i -= 1
            j -= 1
        return ''.join(reversed(ans))