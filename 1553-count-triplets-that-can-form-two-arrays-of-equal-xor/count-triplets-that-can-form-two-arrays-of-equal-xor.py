class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix={0:[-1,1]}
        res,cur=0,0
        for i,v in enumerate(arr):
            cur^=v
            idxSum,cnt=prefix.get(cur,[0,0])
            res+=i*cnt-idxSum-cnt
            prefix[cur]=[idxSum+i,cnt+1]
        return res   