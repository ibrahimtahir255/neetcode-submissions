class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # initialize the stack
        stack = []
        out_list = [0] * len(temperatures)

        for i in range (len(temperatures)):
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                stack_index = stack.pop()
                num_days = i - stack_index
                out_list[stack_index] = num_days
            stack.append(i)
        return out_list
