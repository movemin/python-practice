class Stack:
    def __init__(self):
        self._list = []
    def push(self, value):
        self._list.append(value)
    def pop(self):
        output = self._list[-1]
        del self._list[-1]
        return output
    @property
    def print(self):
        print(self._list)
stack = Stack()
stack.push(10)  # [10]
stack.print
stack.push(20)  # [10, 20]
stack.print
stack.push(30)  # [10, 20, 30]
stack.print
print(stack.pop())     # 30
stack.print
print(stack.pop())     # 20
stack.print
print(stack.pop())     # 10
stack.print
