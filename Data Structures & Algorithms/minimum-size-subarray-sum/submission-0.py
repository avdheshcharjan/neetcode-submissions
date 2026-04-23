class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, total=0,0 #total is the sum of the variable sliding window
        # length=nums+100000 #can be an infinite value, doesn't matter
        length=float('inf')
        # for R in range(len(nums)):
        #     while total >= target:
        #         L=R
        #         length=min(R-L+1, length)
        #         L+=1
        # return 0 if length=float('inf') else length
        for R in range(len(nums)):
            total+=nums[R]
            while total>=target:
                length=min(R-L+1,length)
                total-=nums[L]
                L+=1
        return 0 if length==float('inf') else length