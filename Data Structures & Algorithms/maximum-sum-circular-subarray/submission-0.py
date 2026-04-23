class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
# i was going for duplicating the array, then kadane's algo with the sliding window restriction of len(nums)
# that's a lengthy approach
    #    cir=nums+nums
    #     maxSum=cir[0]
    #     curSum=0
 
        # for n in cir:
        #     curSum=max(0,curSum)
        #     curSum+=n
        #     maxSum=max(curSum,maxSum)
        # return maxSum
        globalMax, globalMin= nums[0], nums[0]
        curMax=curMin=0
        total=0

        for n in nums:
            curMax=max(0+n,curMax+n)
            curMin=min(0+n,curMin+n)
            total +=n
            globalMax=max(curMax,globalMax)
            globalMin=min(curMin,globalMin)
        
        # return max(total-globalMin,globalMax) THERE'S A NAIVE CASE HERE what if every element is negative?      
        return max(total-globalMin,globalMax) if globalMax>0 else globalMax
        """I found the intuition for total - globalMin super confusing, but then it started clicking more for me:

First, understand that in a circular array, the maximum subarray can only exist in two forms:
1. A regular subarray (doesn't wrap)
2. A wrapping subarray (connects end to beginning)

We want to have both of them in our pocket, to compare them and return the greater option!
We already know how the find a regular max subarray (regular Kadane's), so how do we find the wrapping subarray?
Straight up, we just take the full total sum of the entire array (i.e. every element combined), and remove from it the most harming, negative subarray we can find.
Think of it like that, we have 1 chance, 1 cut to make to increase the total value of our wrapping subarray. If you had 1 chance, what would you remove? You'd remove the most HARMING part. the most NEGATIVE part. And how do you find that part? You literally just invert regular Kadane's. Instead of searching for the MAX, you search for the MIN!
You take that discovered disgusting subarray, and just remove it from the total sum! That's your MAXIMUM wrapping subarray right there! It must be.
Then, all you do is just compare that wrapping subarray with the organic 1 pass subarray, and return the greater of the two.

As for the edge case: If all numbers are negative, the intuition that make sense to me is that we really just want to return a subarray of a SINGLE item. Why? Because if the greatest element found is negative, it means every element added to the subarray we return will only decrease the total value (because they're all negative). So we want to return a single item, which is still technically considered a subarray. And that single item will always be stored in globalMax if all numbers are negative. So if globalMax < 0, just return it."""

