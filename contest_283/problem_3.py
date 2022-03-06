# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions):

        head_root = TreeNode(descriptions[0][0])
        cursor_root = TreeNode(descriptions[0][0])

        storage = {}

        for li in descriptions:

            parent = li[0]
            child = li[1]

            #if parent node doesn't exist, create it
            if cursor_root.val != parent and parent not in storage.keys():
                storage[cursor_root.val] = cursor_root
                cursor_root = TreeNode(parent)
                print('created node' + str(parent))
            
            #left child
            if li[2] == 1:
                if child in storage.keys():
                    cursor_root.left = storage[child]
                else:
                    if parent not in storage.keys():
                        storage[cursor_root.val] = cursor_root
                    cursor_root.left = TreeNode(li[1])
                    print('created node' + str(li[1]))
            #right child
            if li[2] == 0:
                if child in storage.keys():
                    cursor_root.right = storage[child]
                else:
                    if parent not in storage.keys():
                        storage[cursor_root.val] = cursor_root
                    cursor_root.right = TreeNode(li[1])
                    print('created node' + str(li[1]))
                if cursor_root.val > head_root.val:
                    head_root = cursor_root
                    

        return head_root




test = Solution()
test.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])