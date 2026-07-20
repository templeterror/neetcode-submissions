class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # empty dict
        count = {}
        
        #empty lists of lists bounded to input array range
        freq =[[]for i in range(len(nums)+1)]

        #populate dict
        for i in nums: #keys = integers, values = frequency
            count[i] = 1 + count.get(i,0)
        
        # c for i(counts), v for values(list)
        for v,c in count.items():
            freq[c].append(v)
        
        res = [] #output list
        for i in range(len(freq) - 1, 0, -1):
            for v in freq[i]:
                res.append(v)
                if len(res) == k:
                    return res

