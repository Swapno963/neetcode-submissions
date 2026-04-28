class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item == "+" or item == "-" or item == "*" or item == "/":
                count = 2
                temp = stack[-1]
                stack.pop(-1)
                while(len(stack) != 0 ):
                    temp2 = stack[-1]
                    stack.pop(-1)
                    if item == "+":
                        res = temp2 + temp
                    elif item == "-":
                        res = temp2 - temp                    
                    elif item == "*":
                        res = temp2 * temp
                    elif item == "/" and temp != 0:
                        res = int(temp2 / temp)
                    stack.append(res) 
                    break
                print("stack : ", stack, "res : ", res)

            else:
                stack.append(int(item)) 
        return stack[0]