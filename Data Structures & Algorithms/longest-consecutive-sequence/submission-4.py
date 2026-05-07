class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       nums = set(nums)
       longest = 0
       for n in nums:
           if n-1 not in nums:
               legth = 0
               while(n+ legth) in nums :
                   legth = legth + 1
                   longest = max(legth,longest)
       return longest
