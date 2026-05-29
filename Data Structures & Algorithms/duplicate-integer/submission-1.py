class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            element = nums[i]
            if element in seen:
                return True
            else:
                seen.add(element)
        return False