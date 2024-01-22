class Solution:
    def reverseWords(self, s: str) -> str:
        l=[]
        t=s.split()
        for i in t:
            i=i[::-1]
            l.append(i)
        return " ".join(l)