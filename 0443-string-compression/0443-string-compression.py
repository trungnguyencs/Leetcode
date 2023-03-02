class Solution:
    def compress(self, chars: List[str]) -> int:
        l = count = 0
        cur = chars[0]
        chars.append(0)
        for r, ch in enumerate(chars):
            if ch == cur:
                count += 1
            else:
                chars[l], cur = cur, ch
                l += 1
                if count > 1:
                    for d in str(count):
                        chars[l] = d
                        l += 1
                count = 1
        return l