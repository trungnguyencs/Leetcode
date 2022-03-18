class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastIdx = {ch: i for i, ch in enumerate(s)}
        stack, seen = [], set()
        for i, ch in enumerate(s):
            if ch in seen: continue
            while stack and ch < stack[-1] and i < lastIdx[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)
        return ''.join(stack)