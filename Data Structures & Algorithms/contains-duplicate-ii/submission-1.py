class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # # O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, min(i+k+1,len(nums))):
        #         if nums[i]==nums[j] and abs(i-j)<=k and i!=j:
        #             return True
        # return False
        window=set()
        L=0
        # for i in range(len(nums)):
        #     if nums[i] in window and i-window[num]
        for R in range(len(nums)):
            if R-L>k:
                window.remove(nums[L])
                L+=1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False