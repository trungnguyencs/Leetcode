class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack, seen = [], set()
        for ch in s:
            if ch not in seen:
                while stack and ch < stack[-1] and counter[stack[-1]]:
                    seen.remove(stack[-1])
                    stack.pop()
                seen.add(ch)
                stack.append(ch)
            counter[ch] -= 1
        return ''.join(stack)