import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #val = nums
        ans = {}
        for i in range(len(nums)):
            ans[nums[i]] = math.prod((nums[:i]+nums[i+1:]))
        answ = []
        for i in nums:
            answ.append(ans[i])

        return answ