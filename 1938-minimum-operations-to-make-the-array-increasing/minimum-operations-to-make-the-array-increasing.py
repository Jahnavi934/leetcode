class Solution:
    def minOperations(self, nums: List[int]) -> int:
        v = 0
        for i in range(1,len(nums)):
            if(nums[i] <= nums[i-1]):
                v += (nums[i-1]-nums[i])+1
                nums[i] = nums[i-1]+1
        print(nums)
        return v