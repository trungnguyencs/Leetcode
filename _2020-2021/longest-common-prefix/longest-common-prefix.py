class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        ans = ''
        for i in range(len(min(strs, key=len))):
            ch = strs[0][i]
            for s in strs:
                if s[i] != ch:
                    return ans
            ans += ch
        return ans
