class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        L = 0

        for i in nums:
            length = 0
            if i-1 not in numSet:

                while (i+length) in numSet:
                    length += 1
            L = max(length, L)
        
        return L

