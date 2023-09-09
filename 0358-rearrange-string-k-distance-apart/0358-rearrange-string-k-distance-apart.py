class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k < 2: return s
        ans = []
        cooling = {}
        heap = [(-freq, c) for c, freq in Counter(s).items()]
        heapify(heap)
        while heap:
            freq, ch = heappop(heap)
            ans.append(ch)
            freq += 1
            if freq != 0:
                cooling[ch] = freq
            if len(ans) >= k and ans[-k] in cooling:
                ch = ans[-k]
                freq = cooling[ch]
                del cooling[ch]
                heappush(heap, (freq, ch))
        return '' if len(ans) < len(s) else ''.join(ans)