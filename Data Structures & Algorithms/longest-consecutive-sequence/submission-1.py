class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sex = set(nums)
        L = 0

        for n in sex:
            if n - 1 not in sex:
                length = 0
                while (n + length) in sex:
                    length += 1
                L = max(L,length)
        
        return L