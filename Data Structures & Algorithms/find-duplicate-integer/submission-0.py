class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            for j in range(i):
                if nums[i]==nums[j]:
                    return nums[i]
                j+=1    
            i+=1
        