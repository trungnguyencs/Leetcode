class Solution:
    def repeatLimitedString(self, s: str, limit: int) -> str:
        ans = []
        counter = Counter(s)
        stack = sorted([ch, freq] for ch, freq in counter.items())
        while stack:
            ch, count = stack.pop()
            if count <= limit:
                ans.append(ch * count)
            else:
                ans.append(ch * limit)
                if not stack:
                    break
                ans.append(stack[-1][0])
                stack[-1][1] -= 1
                if stack[-1][1] == 0: stack.pop()
                stack.append((ch, count - limit))
        return ''.join(ans)