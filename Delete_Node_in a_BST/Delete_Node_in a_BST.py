# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            if root.val == key:
                if not root.left and not root.right:
                    return None
                if root.left and root.right:
                    succ = root.right
                    while succ.left:
                        succ = succ.left
                    root.val = succ.val
                    root.right = self.deleteNode(root.right, succ.val)
                    return root

                return root.left or root.right
                
            if root.val > key:
                if root.left:
                    root.left = self.deleteNode(root.left, key)
                    return root
                return root
            if root.val < key:
                if root.right:
                    root.right = self.deleteNode(root.right, key)
                    return root
                return root
        return None
