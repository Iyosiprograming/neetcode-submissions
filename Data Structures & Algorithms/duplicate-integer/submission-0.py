class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        has_duplicates = len(nums) != len(set(nums))
        
        if has_duplicates == True:
            print("true")
            return True

        else:
            print("false")
            return False

sol = Solution()

sol.hasDuplicate([1,2,3,2,5])