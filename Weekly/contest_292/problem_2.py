# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root) -> int:

        result = 0
        sum_count = [0,0]

        self.dfs(root,sum_count,result)
        return result
        

    def dfs(self,root,sum_count,result):
        if not root:
            return (0,0)
        

        left_total = self.dfs(root.left,sum_count,result)
        right_total = self.dfs(root.right,sum_count,result)

        total = left_total[0] + right_total[0] + root.val
        count = left_total[1] + right_total[1] + 1

        total_average = total//count
        if root.val == total_average:
            result += 1
        
        return (total,count)
        

root = TreeNode(4)
root.left = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right = TreeNode(5)
root.right.right = TreeNode(6)

test = Solution()
print(test.averageOfSubtree(root))
