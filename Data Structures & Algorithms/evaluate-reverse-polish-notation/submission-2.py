class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # intialize a stack
        stack = []

        for item in tokens:
            if item not in ["+", "-", "*", "/"]:
                # push to the stack
                stack.append(item)
            # else (the token is an operator)
            else:
                # if stack empty not empty
                # figure out which operator
                if len(stack) >= 2:
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    
                    if item == '+':
                        result = num2 + num1
                    elif item == '-':
                        result = num2 - num1
                    elif item == '*':
                        result = num2 * num1  
                    elif item == '/':
                        result = num2 / num1
                    else: 
                        continue
            
                # push resutl on the stack
                stack.append(result)

        return int(stack.pop())
        