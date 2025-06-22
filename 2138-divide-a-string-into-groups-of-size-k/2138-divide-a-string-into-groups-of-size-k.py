class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        if len(s) <= k: return [s + fill * (k - len(s))]
        for i in range(0, len(s) - k, k):
            ans.append(s[i:i+k])
        last = s[i+k:]
        ans.append(last + fill * (k - len(last)))
        return ans