class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rol, res = [],[]
        n = len(nums)
        def dfs(i):
            if i == n :
                return res.append(rol[:])

            dfs(i+1)

            rol.append(nums[i])
            dfs(i+1)
            rol.pop()

        dfs(0)

        return  res