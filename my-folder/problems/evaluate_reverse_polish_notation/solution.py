class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for st in tokens:
            if(st=="+"):
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2+n1)
            elif(st == "*"):
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1*n2)
            elif(st == "-"):
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2-n1)
            elif(st == "/"):
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2/n1))
            else:
                stack.append(int(st))
        return stack[0]