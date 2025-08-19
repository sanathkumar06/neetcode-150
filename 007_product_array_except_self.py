class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        prefix = 1
        l = len(nums)
        postfix = 1
        for i in range(l-1):
            prefix *= nums[i]
            res.append(prefix)
        for i in range(l-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
