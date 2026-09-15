
# 706. Design HashMap

class MyHashMap(object):

    def __init__(self):
        self.map = []

    def put(self, key, value):
        map_len = len(self.map)
        for i in range(0, map_len):
            if self.map[i][0] == key:
                self.map[i][1] = value
                return
        self.map.append([key, value])

    def get(self, key):
        map_len = len(self.map)
        for i in range(0, map_len):
            if self.map[i][0] == key:
                return self.map[i][1]
        return -1

    def remove(self, key):
        map_len = len(self.map)
        for i in range(0, map_len):
            if self.map[i][0] == key:
                del self.map[i]
                return

    def print_map(self):
        print(self.map)


class MyHashMapEffective(object):

    map_size = 1000

    def __init__(self):
        self.map = [[] for _ in range(self.map_size)]

    def put(self, key, value):

        index = self.hash_function(key)

        if not self.map[index]:
            self.map[index].append([key, value])
            return

        for i in range(0, len(self.map[index])):
            if self.map[index][i][0] == key:
                self.map[index][i][1] = value
                return
        self.map[index].append([key, value])

    def hash_function(self, key):
        hash_res = key % self.map_size
        return hash_res

    def get(self, key):

        index = self.hash_function(key)

        if not self.map[index]:
            return -1

        sub_map_len = len(self.map[index])

        for i in range(0, sub_map_len):
            if self.map[index][i][0] == key:
                return self.map[index][i][1]

        return -1

    def remove(self, key):

        index = self.hash_function(key)
        if not self.map[index]:
            return

        sub_map_len = len(self.map[index])
        for i in range(0, sub_map_len):
            if self.map[index][i][0] == key:
                del self.map[index][i]
                return

    def print_map(self):
        print(self.map)


if __name__ == "__main__":

    # obj = MyHashMap()
    #
    # obj.put(4, 5)
    # obj.put(2, 6)
    # obj.put(3, 7)
    # obj.print_map()
    #
    # param = obj.get(2)
    # print("param value: ", param)
    #
    # obj.remove(3)
    # obj.print_map()

    obj_v2 = MyHashMapEffective()
    obj_v2.put(4, 5)
    obj_v2.put(2, 6)
    obj_v2.put(3, 7)
    obj_v2.print_map()

    param = obj_v2.get(3)
    print("param value: ", param)

    obj_v2.remove(2)
    obj_v2.print_map()