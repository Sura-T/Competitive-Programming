# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_successor(self, curr):
        curr = curr.right
        while curr is not None and curr.left is not None:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def del_node(node, val):
            if node is None:
                return node

            if node.val > val:
                node.left = del_node(node.left, val)
            elif node.val < val:
                node.right = del_node(node.right, val)
                
            else:
                if node.left is None:
                    return node.right

            
                if node.right is None:
                    return node.left

            
                succ = self.get_successor(node)
                node.val = succ.val
                node.right = del_node(node.right, succ.val)
                
            return node

        return del_node(root, key)