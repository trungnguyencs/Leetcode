class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        for i in range(len(min(strs, key=len))):
            if any(s[i] != strs[0][i] for s in strs):
                break    
            ans.append(strs[0][i])
        return ''.join(ans)