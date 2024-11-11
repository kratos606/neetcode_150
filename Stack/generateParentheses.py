class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openP,closedP):
            if n == openP == closedP :
                res.append(''.join(stack))

            if closedP < openP:
                stack.append(')')
                backtrack(openP,closedP + 1)
                stack.pop()

            if openP < n:
                stack.append('(')
                backtrack(openP + 1,closedP)
                stack.pop()
                
        backtrack(0,0)
        return res
