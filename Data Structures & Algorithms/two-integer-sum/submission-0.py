class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        for i, num in enumerate(nums):
            current = target - num

            if current in hash_map:
                return [hash_map[current], i]

            hash_map[num] = i

sol_1 = Solution()

print(sol_1.twoSum)
