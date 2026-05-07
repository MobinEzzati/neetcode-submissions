class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_index = {}

        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in my_index :
                return [my_index[rest],i]
            my_index[nums[i]] = i
        

       