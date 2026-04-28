class Solution:
    def isValid(self, s: str) -> bool:
        operators = {")":"(", "}":"{", "]":"["}
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                elif operators[i] != stack[-1]:
                    return False
                else:
                    stack.pop()
            # print(stack)
        if len(stack) == 0:
            return True
        return False