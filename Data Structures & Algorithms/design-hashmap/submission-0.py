class MyHashMap:

    def __init__(self):
        self.max_s = 100
        self.hashtable = [[] for i in range(self.max_s)]
        self.hashval = [[] for i in range(self.max_s)]

    def put(self, key: int, value: int) -> None:
        ss = key % self.max_s
        keys = [itt[0] for itt in self.hashtable[ss]]
        if key in keys:
            ind = keys.index(key)
            self.hashtable[ss][ind][1] = value
        else:
            self.hashtable[ss].append([key, value])

    def get(self, key: int) -> int:
        ss = key % self.max_s
        keys = [itt[0] for itt in self.hashtable[ss]]
        if key in keys:
            ind = keys.index(key)
            return self.hashtable[ss][ind][1]
        else:
            return -1


    def remove(self, key: int) -> None:
        ss = key % self.max_s
        keys = [itt[0] for itt in self.hashtable[ss]]
        if key in keys:
            ind = keys.index(key)
            self.hashtable[ss].pop(ind)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)