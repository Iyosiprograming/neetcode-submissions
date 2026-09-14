from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k


solution = Solution()

nums = [1, 1, 1, 2, 2]
val = 1

k = solution.removeElement(nums, val)

print("k:", k)
print("nums:", nums)
print("valid part:", nums[:k])