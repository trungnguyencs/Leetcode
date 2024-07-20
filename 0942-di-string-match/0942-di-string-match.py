class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        start = d = i = s.count('D')
        ans = [start]
        for ch in s:
            if ch == 'D':
                d -= 1
                ans.append(d)
            else:
                i += 1
                ans.append(i)
        return ans