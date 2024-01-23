class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        t=list(s)
        i=0
        j=len(t)-1
        while i < j:
            if t[i].isalpha() and t[j].isalpha():
                t[i],t[j]=t[j],t[i]
                i+=1
                j-=1
            elif t[i].isalpha():
                j-=1
            elif t[j].isalpha():
                i+=1
            else:
                i+=1
                j-=1
        return "".join(t)