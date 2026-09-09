from collections import deque

# 225. Implement Stack using Queues

class MyStack(object):

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        if not self.queue1 and self.queue2:
            self.queue2.append(x)
        elif not self.queue2 and self.queue1:
            self.queue1.append(x)
        else:
            self.queue1.append(x)

    def pop(self):

        if self.empty():
            return None

        if not self.queue2:

            while 1:
                if len(self.queue1) == 1:
                    break
                else:
                    element = self.queue1.popleft()
                    self.queue2.append(element)
            desired_element = self.queue1.popleft()

        else:

            while 1:
                if len(self.queue2) == 1:
                    break
                else:
                    element = self.queue2.popleft()
                    self.queue1.append(element)
            desired_element = self.queue2.popleft()

        return desired_element

    def top(self):

        if self.empty():
            return None

        top_element = self.pop()
        self.push(top_element)
        return top_element

    def empty(self):
        if not self.queue1 and not self.queue2:
            return True
        else:
            return False

if __name__ == "__main__":

    obj = MyStack()

    obj.push(5)
    obj.push(3)
    obj.push(7)

    print(obj.pop())
    print(obj.pop())
    print(obj.pop())

    print(obj.empty())
