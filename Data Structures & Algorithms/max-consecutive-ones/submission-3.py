from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_count = 0
        target = 0
        for num in nums:
            if num == 1:
                current_count += 1
                target = max(target,current_count)
            else:
                current_count = 0

        return target


solution = Solution()

result = solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])

print(result)