class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        final_res = []
        sorted_list = sorted(nums)

        for k in range(len(nums) - 2):

            if k > 0 and sorted_list[k] == sorted_list[k-1]:
                continue

            left = k + 1 
            right = len(nums) - 1
            
            while left < right :
                target = sorted_list[left] + sorted_list[right] + sorted_list[k]

                if target == 0 :
                    final_res.append([sorted_list[left],sorted_list[right],sorted_list[k]])
                 
                    left = left + 1 
                    right = right - 1 
                    

                    while left < right and sorted_list[left] == sorted_list[left - 1] : 
                        left = left + 1 
                    
                    while left < right and sorted_list[right] == sorted_list[right + 1]:
                        right = right - 1          
                elif target < 0 :
                    left = left + 1 
                else : 
                    right = right - 1 
    
        return final_res



                


                


          