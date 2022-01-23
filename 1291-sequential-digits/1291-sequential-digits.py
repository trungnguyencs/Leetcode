class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        q = deque(range(1, 10))
        while q:
            cur = q.popleft()
            if cur > high:
                break
            if cur >= low:
                ans.append(cur)
            lastDigit = cur % 10
            if lastDigit != 9:
                q.append(cur*10 + lastDigit + 1)
        return ans