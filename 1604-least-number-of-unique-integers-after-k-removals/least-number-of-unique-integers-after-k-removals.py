class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        d = list(c.values())
        d.sort()
        s = 0
        i = 0
        while s<=k and i<len(arr):
            s+=d[i]
            i+=1
        return len(d)-i+1 if sum(d)>k else 0