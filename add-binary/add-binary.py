class Solution:
    def addBinary(self, a: str, b: str) -> str:
        rev_a, rev_b = a[::-1], b[::-1]
        i, j, carry = 0, 0, 0
        ans = []
        while i < len(a) or j < len(b) or carry:
            if i < len(a):
                carry = carry + 1 if rev_a[i] == '1' else carry
                i += 1
            if j < len(b):
                carry = carry + 1 if rev_b[j] == '1' else carry
                j += 1
            ans.append(str(carry % 2))
            carry //= 2
        return ''.join(ans[::-1])
