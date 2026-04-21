class MyHashSet:

    def __init__(self):
        self.maxsize = 1000
        self.hashtable = [[] for i in range(self.maxsize)]

    def add(self, key: int) -> None:
        ss = key % self.maxsize
        if key not in self.hashtable[ss]:
            self.hashtable[ss].append(key)

    def remove(self, key: int) -> None:
        ss = key % self.maxsize
        cc = self.contains(key)
        if cc:
            self.hashtable[ss].remove(key)

    def contains(self, key: int) -> bool:
        ss = key % self.maxsize
        return self.hashtable[ss].count(key) > 0


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)