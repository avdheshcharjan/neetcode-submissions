class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False

        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                
                top = stack.pop()
                
                if char == ")" and top != "(":
                    return False
                if char == "]" and top != "[":
                    return False
                if char == "}" and top != "{":
                    return False
        
        return len(stack) == 0    
        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        # return s == ''

