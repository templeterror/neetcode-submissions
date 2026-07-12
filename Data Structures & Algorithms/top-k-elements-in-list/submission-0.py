class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for i in nums:
            seen[i] = seen.get(i,0) + 1 # mapping is done key(integers): values(frequencies)
        
        s = list(seen.items()) # get key value tuples and put them in a list

        pairs = sorted(s, key=lambda p: p[1], reverse=True)

        return [p[0] for p in pairs[:k]] 