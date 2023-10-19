class Solution:
    def countTime(self, time: str) -> int:
        ans = 1
        if time[-2] == '?': ans *= 6
        if time[-1] == '?': ans *= 10
        if time[0:2] == '??': ans *= 24
        elif time[0] == '?':
            ans *= 3 if time[1] in '0123' else 2
        elif time[1] == '?':
            ans *= 4 if time[0] == '2' else 10
        return ans