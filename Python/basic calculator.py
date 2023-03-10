class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        pre_op = '+'
        num = 0
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if (not char.isdigit() and char != ' ') or i == len(s) - 1:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack[-1] = stack[-1] * num
                elif pre_op == '/':
                    stack[-1] = int(stack[-1] / num)
                pre_op = char
                num = 0
        return sum(stack)

s = input("Enter the expression: ")

sol = Solution()

result = sol.calculate(s)

print("Result:", result)
