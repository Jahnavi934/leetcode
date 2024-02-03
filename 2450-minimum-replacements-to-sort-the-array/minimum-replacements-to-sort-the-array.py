class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        maxi = nums[len(nums)-1]
        ans = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > maxi:
                v = nums[i]//maxi
                if nums[i] % maxi:
                    v += 1
                maxi = nums[i]//v
                ans += v-1
            else:
                maxi = nums[i]
        return ans
                