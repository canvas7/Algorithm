#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (72.13%)
# Likes:    480
# Dislikes: 0
# Total Accepted:    137.6K
# Total Submissions: 189.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
# 
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最大深度 3 。
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # DFS 递归
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        """ # DFS 非递归 栈
        cur, stack, depth, max_depth = root, [], 0, 0
        while cur or stack:
            while cur:
                depth += 1
                stack.append((cur, depth))
                cur = cur.left
            top, depth = stack.pop()
            if depth > max_depth:
                max_depth = depth
            cur = top.right
        return max_depth """
        
        """ # BFS 迭代 队列 
        if not root:
            return 0
        depth = 0
        q = [root]
        while q:
            depth += 1
            for i in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return depth """

# @lc code=end

