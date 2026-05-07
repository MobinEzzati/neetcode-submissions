class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHash = {}

        for i in range(len(nums)):
            myHash[nums[i]] = i
        
        
    
        for i in range(len(nums)) : 
            rest = target - nums[i]
            if rest in myHash and i != myHash[rest]:
                return [i,myHash[rest]]
            