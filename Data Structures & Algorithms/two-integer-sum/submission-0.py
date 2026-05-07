class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        numbers = {}
        counter = 0
        while counter < len(nums):
            rest = target - nums[counter]
            if rest in numbers:
                return [numbers[rest], counter]
            numbers[nums[counter]] = counter
            counter += 1

