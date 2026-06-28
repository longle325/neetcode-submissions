class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        subset = []
        def dfs(i):
            if i>= n: 
                res.append(subset.copy())
                return
            # Choose nums[i]
            subset.append(nums[i])
            dfs(i+1)
            # Not choose nums[i]
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res





        