class Solution:
    def maxSubArray(self, nums) :
        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        for i in range (1,len(nums)):
            if dp[i-1]>0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i]=nums[i]
        # print("dp:",dp)
        return max(dp)

res=Solution().maxSubArray(nums = [5,4,-1,7,8])
print("res:",res)