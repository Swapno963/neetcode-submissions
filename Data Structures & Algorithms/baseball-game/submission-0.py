class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        for item in operations:
            if item == "+":
                # new record: sum of previous 2 number
                stack.append(stack[-1] + stack[-2])

            elif item == 'D':
                # new record: double of previous score
                stack.append(stack[-1] * 2)

            elif item == "C":
                #  remove last element
                stack.pop()
            else:
                stack.append(int(item))

        
        for item in stack:
            sum += item
        return sum