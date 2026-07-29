class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #empty dict
        hi = {}

        # empty lists of lists, +1 to length because freq starts from i=1
        freq = [[] for i in range(len(nums) + 1)]

        #transfer nums to dict
        #key = number, value = frequency
        for i in nums:
            hi[i] = hi.get(i, 0) + 1

        #now do the bucket sort to freq
        #indeces are count/frequencies = values
        #values are the integers=keys
        for key,v in hi.items():
            freq[v].append(key)
        
        #now output list
        res = []

        #populate res by looping on Freq until len = k
        #start at the end cuz higher freqs at end
        for i in range(len(freq)-1, 0, -1):
            for v in freq[i]:
                res.append(v)
                if len(res) == k:
                    return res
        
