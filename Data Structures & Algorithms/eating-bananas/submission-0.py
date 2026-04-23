class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # L,R=0, len(p)-1
        L,R=1, max(piles)
        res=float('inf')
        #k has a range from 1 to max(p[i]) so we have to apply BS here
        #len(p)<=h
        while L<=R:
            k=(L+R)//2
            hours=0
            for p in piles:
                hours+=math.ceil(p/k)
            if hours <= h:
                res = min(res, k)
                R=k-1
            else:
                L=k+1
        return res    
