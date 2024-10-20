"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        charRead = 0
        loop = 0
        while n > 0:
            buf4 = ['']*4
            count = read4(buf4)
            charReadThisLoop = min(n, count)
            if charReadThisLoop <= 0: break
            for i in range(charReadThisLoop):
                buf[4*loop + i] = (buf4[i])
            charRead += charReadThisLoop
            n -= charReadThisLoop
            loop += 1
        return charRead