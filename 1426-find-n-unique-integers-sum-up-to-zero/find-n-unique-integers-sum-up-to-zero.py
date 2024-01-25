class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = list(range(-(n // 2), n // 2 + 1))
        if n % 2 == 0:
            result.remove(0)  # Remove 0 if n is even
        return result

# Example usage:
solution = Solution()
print(solution.sumZero(5))  # Output: [-2, -1, 0, 1, 2]
print(solution.sumZero(3))  # Output: [-1, 0, 1]
print(solution.sumZero(1))