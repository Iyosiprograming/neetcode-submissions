class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums + nums
        return ans


solution_1 = Solution()

test = solution_1.getConcatenation([1, 2, 3, 4])

print(test)