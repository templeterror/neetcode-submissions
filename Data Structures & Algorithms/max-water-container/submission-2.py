class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        area = 0
        for i, n in enumerate(heights):
            for j in range(i + 1, len(heights)):
                v = heights[j]
                area1 = min(n,v) * (j-i)
                area = max(area,area1)
        
        return area
