class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # n=len(nums)
        # ans=[]
        # for i in range(2n):
        #     ans[i]==nums[i] && ans[i+n]== nums[i]
            

        # return ans
        #above is the wrong code
        #below are two methods
        return nums + nums

# or 
        # n = len(nums)
        # ans = []

        # for i in range(2 * n):
        #     ans.append(nums[i % n])

        # return ans