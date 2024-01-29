class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=min(len(word1),len(word2))
        k=max(len(word1),len(word2))
        o=[]
        for i in range(l):
            o.append(word1[i])
            o.append(word2[i])
        p=len(o)//2
        for i in range(p,k):
                if k==len(word1):
                    o.append(word1[i])
                else:
                    o.append(word2[i])
        return "".join(o)
