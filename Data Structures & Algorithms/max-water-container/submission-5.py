class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        h = heights
        area = 0
        l, r = 0, len(heights) - 1
        #i am shit at this goddamn
        
        while l<r:
            area1 = min(h[l],h[r]) * (r-l)

            area = max(area, area1)
            

            if h[l] >= h[r]:
                r-=1
            elif h[l]<h[r]:
                l+=1
        
        return area

