class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i not in set(['*','+','-','/']):
                stack.append(int(i))
            else:
                x = stack.pop()
                y = stack.pop()
                stack.append(int(eval(f"{float(y)} {i} {x}")))
                
        return stack[0]
