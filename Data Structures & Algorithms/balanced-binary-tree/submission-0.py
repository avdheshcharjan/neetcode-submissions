# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True
        
        # F/S pointers?
        # fast, slow = root
        # while fast and fast.next:
        #     slow=root.left
        #     fast=root.right.right

        
        # if (fast - slow > 1):
        #     return False
        # diff=abs(self.isBalanced(root.left)-self.isBalanced(root.right))

        # if (diff >1):
        #     return False


        # self.isBalanced(root.left)
        # self.isBalanced(root.right)

        def dfs(root):
            if not root: return [True,0]
            #index 0 returns Boolean, index 1 returns height
            left, right= dfs(root.left), dfs(root.right)
            balanced= abs(left[1]-right[1]) <=1 and left[0] and right[0]

            return [balanced,max(left[1],right[1]) + 1]
            # return the balanced, height
        
        return dfs(root)[0]
        
        

