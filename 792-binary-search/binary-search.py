class Solution:
    def search(self, nums: List[int], target: int) -> int:
        v=0
        if target not  in nums:
            return -1
        else:
            v=nums.index(target)
            return v