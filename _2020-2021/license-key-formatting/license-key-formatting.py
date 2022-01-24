class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '')
        ans = []
        for i, ch in enumerate(s):
            ans.append(ch.upper())
            if (len(s)-1 - i) % k == 0:
                ans.append('-')
        return ''.join(ans).strip('-')
    