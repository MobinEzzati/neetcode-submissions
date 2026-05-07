class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackCalculator = []

        for item in tokens:

            if item == "+":
                 a = int(stackCalculator.pop())
                 b = int(stackCalculator.pop())
                 stackCalculator.append(a+b)
            elif item == "*":
                 print(stackCalculator)
                 a = int(stackCalculator.pop())
                 b = int(stackCalculator.pop())
                 stackCalculator.append(int(a * b))

            elif item == "-":
                a = int(stackCalculator.pop())
                b = int(stackCalculator.pop())
                stackCalculator.append(int(b-a))

            elif item == "/":
                a = int(stackCalculator.pop())
                b = int(stackCalculator.pop())
                stackCalculator.append(int(b / a))
            else:
                stackCalculator.append(int(item))

        return stackCalculator[0]
        