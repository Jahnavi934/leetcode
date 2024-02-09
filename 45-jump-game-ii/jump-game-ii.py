class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n < 2:
            return 0
        count = 1
        i=0
        while i < n:
            if i+nums[i] >= n-1:
                return count
            temp_max = 0
            temp_index = i
            for j in range(i+1, i+nums[i]+1):
                weight = nums[j]+j if nums[j] > 0 else 0
                if weight > temp_max:
                    temp_max = weight
                    temp_index = j - 1
            i = temp_index
            count+=1
            i+=1
        return count