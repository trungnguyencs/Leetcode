class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(["%d:" %len(s) + s for s in strs])

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        left = 0
        while left < len(s):
            right = s.find(':', left)
            length = int(s[left:right])
            ans.append(s[right + 1: right + length + 1])
            left = right + length + 1
        return ans

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))