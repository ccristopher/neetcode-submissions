class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []

        for i in tokens:
            if i == '+':
                my_stack.append(my_stack.pop() + my_stack.pop())
            
            elif i == '-':
                a, b = my_stack.pop(), my_stack.pop()
                my_stack.append(b - a)
            
            elif i == '*':
                my_stack.append(my_stack.pop() * my_stack.pop())
            
            elif i == '/':
                a, b = my_stack.pop(), my_stack.pop()
                my_stack.append(int(b / a))
            
            else:
                my_stack.append(int(i))
        
        return my_stack[0]