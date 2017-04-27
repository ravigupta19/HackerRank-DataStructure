class Queue(object):
    def __init__(self):
        self.que = []
        self.front = None
        self.end = None

    def enqueue(self, data):
        self.que.append(data)
        self.end = self.que[-1]
        if self.front is None:
            self.front = self.que[0]

    def dequeue(self):
        try:
            self.que.pop()
            self.front = self.que[0]
        except IndexError:
            self.front = None
            self.end = None

    def getTop(self):
        return self.front


que = Queue()
for i in range(int(input())):
    oper = input().split()
    if oper[0] == '1':
        que.enqueue(oper[1])
    elif oper[0] == '2':
        que.dequeue()
    else:
        print(que.getTop())
    print(que.que)