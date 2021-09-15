# basic queue on two stacks
import sys


class Queue:
    def __init__(self):
        self.instack=[]
        self.outstack=[]
        self.len = 0

    def push(self, element):
        if self.len < size:
            self.instack.append(element)
            self.len += 1
        else:
            print('error')

    def pop(self):
        if self.len <= 0:
            return None
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        self.len -= 1
        return self.outstack.pop()

    def peek(self):
        if self.len <= 0:
            return None
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack[len(self.outstack)-1]


    def sizeof(self):
        return self.len


if __name__ == "__main__":
    q = Queue()
    n = int(sys.stdin.readline().rstrip())
    size = int(sys.stdin.readline().rstrip())
    for i in range(n):
        command = [str(x) for x in sys.stdin.readline().rstrip().split(' ')]
        if command[0] == 'peek':
            print(q.peek())
        if command[0] == 'pop':
            print(q.pop())
        if command[0] == 'push':
            q.push(int(command[1]))
        if command[0] == 'size':
            print(q.sizeof())




