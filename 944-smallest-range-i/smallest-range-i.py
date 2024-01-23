class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        a=min(nums)
        b=max(nums)
        if(b-a-2*k)>0:
            return b-a-2*k
        return 0