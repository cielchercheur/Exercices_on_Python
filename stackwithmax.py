# stack with max element realisation
import sys

class StackMax:
    stack = list()
    list_of_maxs = list()
    # push, pop, get_max

    def push(self, value):
        self.stack.append(value)
        if len(self.list_of_maxs) == 0 or self.list_of_maxs[-1] < value:
            self.list_of_maxs.append(value)
        else:
            self.list_of_maxs.append(self.list_of_maxs[-1])

    def pop(self):
        if len(self.stack) == 0:
            print('error')
            return
        value = self.stack.pop()
        _ = self.list_of_maxs.pop()
        return value

    def get_max(self):
        if len(self.list_of_maxs) == 0:
            return None
        return self.list_of_maxs[-1]


if __name__ == "__main__":
    stack = StackMax()
    n = int(sys.stdin.readline().rstrip())
    for i in range(n):
        command = [str(x) for x in sys.stdin.readline().rstrip().split(' ')]
        if command[0] == 'get_max':
            print(stack.get_max())
        if command[0] == 'pop':
            stack.pop()
        if command[0] == 'push':
            stack.push(int(command[1]))
