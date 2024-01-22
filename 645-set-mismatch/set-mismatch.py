class Solution(object):
    def findErrorNums(self, nums):
        a = sum(nums) - sum(set(nums))
        b = sum(range(1, len(nums) + 1))
        c = sum(set(nums))
        d = b - c

        return [a, d]