class Solution:
    def isValid(self, s: str) -> bool:
        """
        U:
        Edge cases:
        if s = "" -> true
        if len(s) is an odd number -> false

        M:
        data structure: stack
        pattern matching: push if opening, pop and comapre when closing
        """

        # initialize a stack
        stack = []

        # initlaize a dict with valid opening and closing parenthesis pairs
        # (closing as keys and openings as vals)
        my_dict = {')':'(', '}':'{', ']':'['}
        
        for item in s:
            # if item is a closing paren
            if item in my_dict:
                # if stack empty, return false
                if len(stack) == 0:
                    return False
                # pop the stack, compare, if nt equal return false 
                if stack.pop() != my_dict[item]:
                    return False
            # if item opening paren append it to stack
            if item not in my_dict:
                stack.append(item)
        return len(stack) == 0
        

    
        