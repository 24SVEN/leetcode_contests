# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions):


        #Great solution and easy to understand.
        #https://leetcode.com/problems/create-binary-tree-from-descriptions/discuss/1823678/Python-Solution-using-HashMap-with-Steps


        #keys are node values while value is list of [tree node, has_parent]
        hash_map = {}

        for li in descriptions:
            parent_val = li[0]
            child_val = li[1]
            isLeft = li[2]

            if hash_map.get(parent_val,None) is None:
                hash_map[parent_val] = [TreeNode(parent_val),False]
            if hash_map.get(child_val,None) is None:
                hash_map[child_val] = [TreeNode(child_val),False]
            hash_map[child_val][1] = True

            if isLeft:
                hash_map[parent_val][0].left = hash_map[child_val][0]
            else:
                hash_map[parent_val][0].right = hash_map[child_val][0]

        
        for key,val in hash_map.items():
            if val[1] is False:
                return val[0] 

        return None




test = Solution()
test.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])