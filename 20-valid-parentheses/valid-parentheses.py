class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        
        for ch in s:
            if ch in pairs:
                if stack and stack[-1] == pairs[ch]: #проверка что стэк не пуст
                    stack.pop() 
                else:
                    return False  
            else:
                stack.append(ch)  
        
        return len(stack) == 0