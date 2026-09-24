
# 2526. Find Consecutive Integers from a Data Stream

class DataStream(object):

    def __init__(self, value, k):
        self.value = value
        self.k = k
        self.counter = 0

    def consec(self, num):
        if num == self.value:
            self.counter += 1
        else:
            self.counter = 0

        if self.counter >= self.k:
            return True
        else:
            return False


if __name__ == "__main__":

    data_stream = DataStream(4, 3)
    print(data_stream.consec(4))
    print(data_stream.consec(4))
    print(data_stream.consec(4))
    print(data_stream.consec(3))