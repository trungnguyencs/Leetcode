class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '').upper()
        r = len(S) % K
        ans = []
        for i, ch in enumerate(S):
            ans.append(ch)
            if (i-r+1) % K == 0:
                ans.append('-')
        return ''.join(ans).strip('-')