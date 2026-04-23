class Solution:
    # used a hint for else: if heights[l]<heights[r]
    def maxArea(self, heights: List[int]) -> int:
        max=0
        l,r = 0, len(heights)-1
        # if l<=r:
        while l<=r:
            area = min(heights[l],heights[r]) * (r-l)
            if area > max:
                max=area
            else:
                if heights[l]<heights[r]:
                    l+=1
                else:
                    r-=1

        return max    