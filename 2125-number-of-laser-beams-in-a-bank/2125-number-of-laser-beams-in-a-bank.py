class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = ans = 0
        for row in bank:
            cur = row.count('1')
            if cur == 0: continue
            ans += cur * prev
            prev = cur
        return ans