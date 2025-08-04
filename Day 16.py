#Day 16: Data Structures – Stacks (List as Stack + Stack Use Case(s))
from inspect import stack
from operator import truediv


#Create a Stack class with push, pop, peek, is_empty, and size methods.
class Stack:
    def __init__(self):
        self.stack = []
        self.toppointer = -1


    def size(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)
        self.toppointer += 1
        return self.stack

    def is_empty(self):
        if self.toppointer == -1:
            return  True
        else:
            return  False


    def pop(self):
       if self.is_empty():
           raise IndexError("Stack is empty")
       else:
           self.toppointer -= 1
           return self.stack.pop()


    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")

        else:
         return self.stack[self.toppointer]


#Use a list to reverse a user’s input string using stack behavior.
def string_reverse(string):
    reverseword = list(string)
    # char = reverseword[len(reverseword) -1]
    # for char in reverseword:
    reverselist = []
    for i in range(len(reverseword) -1, -1,-1):
        reverselist.append(reverseword[i])

    print( ''.join(reverselist))


string_reverse("madam")

#Given a postfix expression like "231*+9-", evaluate it using a stack.
def postfix(expression):
    stack = []
   
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            if char == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b +a)

            else:
             if char == "-":
                 a = stack.pop()
                 b = stack.pop()
                 stack.append(b - a)

             else:
                 if char == "*":
                     a = stack.pop()
                     b = stack.pop()
                     stack.append(b * a)
                 else:
                     if char == "/":
                         a = stack.pop()
                         b = stack.pop()
                         stack.append(b / a)
    print(stack)


postfix("231*+9-")
