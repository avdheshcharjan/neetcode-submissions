class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # seen_set = set()
        # for nums[i] in nums:
        #     diff=target - nums[i]
        #     if diff in seen_set:
        #         return num, diff
        prevMap = {} #val:index
        for i, n in enumerate(nums): # enumerate is particularly useful for simplifying loops where you need access to both the element and its position, removing the need for manually managing a separate counter variable
            diff = target - n
            if diff in prevMap:
                return [ prevMap[diff], i]
            prevMap[n] = i