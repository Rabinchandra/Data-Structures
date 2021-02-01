class Stack:
    def __init__(self):
        self.list = [None] * 10
        self.top = -1
    
    def push(self, x):
        self.top = self.top + 1
        self.list[self.top] = x
    
    def pop(self):
        if self.top > -1:
            self.top = self.top - 1
    
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    
    def get(self):
        if self.top == -1:
            return None
        return self.list[self.top]


stack_1 = Stack()

stack_1.push(1)
stack_1.push(2)

# print(stack_1.list)
# print(stack_1.top)
print(stack_1.get())

# stack_1.pop()
# stack_1.pop()

# print(stack_1.isEmpty())