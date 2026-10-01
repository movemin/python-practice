class Queue:
    def __init__(self):
        self.__list = []
    def enqueue(self, value):
        self.__list.append(value)
    def dequeue(self):
        output = self.__list[0]
        del self.__list[0]
        return output

que = Queue()
que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
print(que.dequeue())
print(que.dequeue())
print(que.dequeue())