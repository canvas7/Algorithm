#
# @lc app=leetcode.cn id=336 lang=python3
#
# [336] 回文对
#
# https://leetcode-cn.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (33.07%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    2.9K
# Total Submissions: 8.6K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# 给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。
# 
# 示例 1:
# 
# 输入: ["abcd","dcba","lls","s","sssll"]
# 输出: [[0,1],[1,0],[3,2],[2,4]] 
# 解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
# 
# 
# 示例 2:
# 
# 输入: ["bat","tab","cat"]
# 输出: [[0,1],[1,0]] 
# 解释: 可拼接成的回文串为 ["battab","tabbat"]
# 
#

# @lc code=start
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
# @lc code=end

