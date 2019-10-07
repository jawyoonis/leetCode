class Solution:
    def rob(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]= max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            max_value= max(dp[i-1], nums[i]+dp[i-2] )
            dp[i]= max_value
        return dp[-1]
arr=[1,2,3]


print(Solution().rob(arr))
