class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        seen = set([start])
        q = deque([[start, 0]])
        while q:
            cur, step = q.popleft()
            if cur == goal: return step
            if not 0 <= cur <= 1000: continue
            for num in nums:
                if not cur + num in seen:
                    seen.add(cur + num)
                    q.append([cur + num, step + 1])
                if not cur - num in seen:
                    seen.add(cur - num)
                    q.append([cur - num, step + 1])
                if not cur ^ num in seen:
                    seen.add(cur ^ num)
                    q.append([cur ^ num, step + 1])
        return -1