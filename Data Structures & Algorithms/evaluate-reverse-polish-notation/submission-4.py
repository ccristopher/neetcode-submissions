class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []

        for i in range(len(tokens)):
            val = tokens[i]

            if val.isdigit() or (val.startswith('-') and val[1:].isdigit()):
                my_stack.append(val)
            
            else:
                val1 = my_stack.pop()
                val2 = my_stack.pop()
                my_stack.append(int(eval(str(val2) + tokens[i] + str(val1))))
        
        return int(my_stack[0])