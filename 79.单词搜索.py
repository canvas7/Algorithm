#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (40.43%)
# Likes:    337
# Dislikes: 0
# Total Accepted:    42.8K
# Total Submissions: 104.6K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 示例:
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.
# 
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS
        def dfs(board, i, j, word):
            if not word:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
                return False
            tmp = board[i][j]
            board[i][j] = '#'
            res = dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:]) or dfs(board, i, j+1, word[1:]) or dfs(board, i, j-1, word[1:])
            board[i][j] = tmp
            return res 

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word):
                    return True
        return False
# @lc code=end

