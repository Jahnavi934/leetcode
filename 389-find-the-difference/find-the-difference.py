class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        c=0
        for cs in s:c ^=ord(cs)
        for ct in t:c^=ord(ct)
        return chr(c)
        