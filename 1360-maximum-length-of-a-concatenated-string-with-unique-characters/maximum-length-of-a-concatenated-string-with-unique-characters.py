class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        res = []
        for i in range(1,n+1):
            k = list(combinations(arr,i))
            for j in k:
                s = ''.join(j)
                if len(set(s)) == len(s):
                    res.append(len(s))
        if len(res):
            return max(res)
        return 0