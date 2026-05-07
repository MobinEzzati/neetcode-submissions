class MinStack:

     def __init__(self):
        self.miniStack =[]


     def push(self, val: int) -> None:
        self.miniStack.append(val)



     def pop(self) -> None:

         if len(self.miniStack) != 0:
             self.miniStack.pop()

     def show(self):
        print(self.miniStack)


     def top(self) -> int:
         if self.miniStack:
             return  self.miniStack[-1]


     def getMin(self) -> int:
         if self.miniStack:


             min = self.miniStack[0]
             length = len(self.miniStack)
             for i in range(0, length ):
               if self.miniStack[i] < min:
                   min = self.miniStack[i]
         return min