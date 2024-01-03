class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0
        for s in bank:
            cur = s.count('1')
            if cur == 0:
                continue
            else:
                ans += cur * prev
                prev = cur
        return ans