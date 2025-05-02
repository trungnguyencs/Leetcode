class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'L' + dominoes + 'R'
        ans = ""
        l = 0
        for r in range(1, len(dominoes)):
            if dominoes[r] == '.':
                continue
            d = r - l - 1
            if l != 0:
                ans += dominoes[l]
            if dominoes[l] == dominoes[r]:
                ans += dominoes[l] * d
            elif dominoes[l] == 'L' and dominoes[r] == 'R':
                ans += '.' * d
            else:
                ans += 'R' * (d//2) + '.' * (d % 2) + 'L' * (d//2)
            l = r
        return ans