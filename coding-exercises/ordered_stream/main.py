
# 1656. Design an Ordered Stream

class OrderedStream(object):

    def __init__(self, n):
        self.n = n
        self.stream = [None for _ in range(self.n)]
        self.on_queue = 0

    def insert(self, id_key, value):

        id_key_index = id_key - 1

        # store the incoming value
        self.stream[id_key_index] = value

        # if current element in queue arrived
        if self.on_queue == id_key_index:
            # append the element in queue and greater than him - only the nearby values
            # return until None - if not meet None return values which append so far
            return_list = []
            for i in range(id_key_index, self.n):
                if self.stream[i] is not None:
                    return_list.append(self.stream[i])
                    self.on_queue += 1
                else:
                    return return_list

            return return_list

        # if incoming element not match the one in queue
        else:
            return []

# Your OrderedStream object will be instantiated and called as such:
if __name__ == "__main__":

    # example:
    # idKey:        1     2     3     4     5
    # init:      [None, None, None, None, None]   on_queue=0 (id_key=1)    return []
    # insert(4): [None, None, None, ddd,  None]   on_queue=0 (id_key=1)    return []
    # insert(5): [None, None, None, ddd,  eee ]   on_queue=0 (id_key=1)    return []
    # insert(1): [aaa,  None, None, ddd,  eee ]   on_queue=1 (id_key=2)    return [aaa]
    # insert(2): [aaa,  bbb,  None, ddd,  eee ]   on_queue=2 (id_key=3)    return [bbb]
    # insert(3): [aaa,  bbb,  ccc,  ddd,  eee ]   on_queue=5 (finished)    return [ccc, ddd, eee]

    obj = OrderedStream(5)
    res = obj.insert(4,"ddd")
    print(res)
    res = obj.insert(5, "eee")
    print(res)
    res = obj.insert(1, "aaa")
    print(res)
    res = obj.insert(2, "bbb")
    print(res)
    res = obj.insert(3, "ccc")
    print(res)