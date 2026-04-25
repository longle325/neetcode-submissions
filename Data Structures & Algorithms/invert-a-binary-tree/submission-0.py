# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
# Base case: Nếu node rỗng thì dừng
        if not root:
            return None
        
        # Đổi chỗ nhanh (Swap) nhánh trái và phải bằng cú pháp Python
        root.left, root.right = root.right, root.left
        
        # Đệ quy lật tiếp tục cho phần dưới của nhánh trái và nhánh phải
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # Trả về gốc của cây đã lật
        return root

        