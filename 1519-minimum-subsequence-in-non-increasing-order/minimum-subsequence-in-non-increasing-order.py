class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        n=len(nums)
        pre=[0]*n
        pre[0]=nums[0]
        for i in range(1,n):
            pre[i]=pre[i-1]+nums[i]
        res=0
        for i in range(n):
            #print(pre[i],abs(pre[i]-pre[-1]))
            if pre[i]>abs(pre[i]-pre[-1]):
                return nums[:i+1]
            
            
        