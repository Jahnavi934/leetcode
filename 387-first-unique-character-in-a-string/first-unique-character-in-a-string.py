class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return -1

        char_count = {}
        for ch in s:
            char_count[ch] = char_count.get(ch, 0) + 1

        for i in range(n):
            ch = s[i]
            if char_count[ch] == 1:
                return i

        return -1
        