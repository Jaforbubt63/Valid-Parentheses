class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        
        for ch in s:
            if ch in "({[":
                stk.append(ch)
            else:
                if len(stk) == 0:
                    return False
                
                last_item = stk.pop()
                if ch == ')':
                    if last_item != '(':
                        return False
                    elif ch == '}':
                        if last_item != '{':
                            return False
                    elif ch == ']':
                        if last_item != '[':
                            return False
                        
        return stk ==[]
            
                    