class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        counter =0

        for pointer_fast in range(1, len(nums)):
            if nums[pointer_fast]!=nums[counter]:
                counter+=1
                nums[counter]=nums[pointer_fast]

        return counter + 1 #because counter is an index
        