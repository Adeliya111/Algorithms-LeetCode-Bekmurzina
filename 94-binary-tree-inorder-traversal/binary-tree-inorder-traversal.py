class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = [] #результат
        st = [] #хранилище узлов
        curr = root #текущий узел
        
        while st or curr:
            while curr:
                st.append(curr)
                curr = curr.left
            
            curr = st.pop()
            res.append(curr.val)

            curr = curr.right
        
        return res