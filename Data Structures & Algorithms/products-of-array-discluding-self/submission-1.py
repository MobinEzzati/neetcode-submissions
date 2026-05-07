
class Solution:


      def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        print(length)
        answer = [0] * length
        left = [0] * length
        right = [0] * length
        left[0] = 1
        right[length - 1] = 1
        for i in range(1 , length):
            left[i] = nums[i-1] * left[i-1]
        print(left)
        for i in reversed(range(length - 1)):
            right[i] = nums[i + 1] * right[i + 1]

        for j in range(length):
            print(j)
            answer[j] = left[j] * right[j]
        return answer
