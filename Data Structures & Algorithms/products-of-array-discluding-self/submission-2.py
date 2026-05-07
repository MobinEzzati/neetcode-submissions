class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postFix = [1] * len(nums)

        res = []
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for j in range(len(nums)-2, -1 , -1):
            postFix[j] = postFix[j+1] * nums[j+1]
        

        for item1,item2 in zip(prefix,postFix):
            res.append(item1 * item2)
        

        return res

        