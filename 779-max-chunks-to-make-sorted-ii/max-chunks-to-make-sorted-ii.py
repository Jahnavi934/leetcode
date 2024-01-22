class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        v =arr.copy()
        arr.sort()
        sum1,sum2,c = 0,0,0
        for i in range(len(arr)):
            sum1 += arr[i] 
            sum2 += v[i]
            if sum1 == sum2:
                c += 1
        return c