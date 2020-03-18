#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (76.36%)
# Likes:    492
# Dislikes: 0
# Total Accepted:    68.9K
# Total Submissions: 89.8K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """ # DFS 回溯记录结点
        def dfs(start, path):
            res.append(path)
            for i in range(start, len(nums)):
                dfs(i+1, path+[nums[i]])
        res = []
        dfs(0, [])
        return res """
        # DFS 回溯记录深度
        def dfs(start, path):
            if len(path) == k:
                res.append(path[:])
            for i in range(start, n):
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
        res = []
        n = len(nums)
        for k in range(n+1):
            dfs(0, [])
        return res
# @lc code=end

