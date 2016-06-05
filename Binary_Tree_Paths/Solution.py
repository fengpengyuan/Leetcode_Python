__author__ = 'fengpeng'


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        res = []
        self.dfs(root, "", res)
        return res

    # def dfs(self, root, path, res):
    # if not root:
    #         return
    #     if path:
    #         path = path + "->" + str(root.val)
    #     else:
    #         path = str(root.val)
    #     if not root.left and not root.right:
    #         res.append(path)
    #     self.dfs(root.left, path, res)
    #     self.dfs(root.right, path, res)

    def dfs(self, root, path, res):
        if not root:
            return
        path += str(root.val)
        if not root.left and not root.right:
            res.append(path)
        self.dfs(root.left, path + "->", res)
        self.dfs(root.right, path + "->", res)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.right = TreeNode(5)
root.right.right = TreeNode(6)

print Solution().binaryTreePaths(root)