class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        st = []
        curr = root
        
        while st or curr:
            while curr:
                res.append(curr.val)
                st.append(curr)
                curr = curr.right
            
            curr = st.pop()
            curr = curr.left
        
        return res[::-1]  #переворот для postorder
