class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        # for i in tokens:
        #     if i is in range(0-9):
        #         int(i)
        #         stack.push()
        #     else:
        #         stack.pop()
        #         stack.pop()
        for i in tokens:
            if i == "+":
                stack.append(stack.pop()+ stack.pop())
            elif i == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif i == "*":
                stack.append(stack.pop()* stack.pop()) 
            elif i == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/(a)))
            else:
                stack.append(int(i))
        return stack[0]