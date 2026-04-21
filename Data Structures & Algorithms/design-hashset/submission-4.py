class MyHashSet:

    def __init__(self):
        self.dictdd = {}
        

    def add(self, key: int) -> None:
        self.dictdd[key] = None

    def remove(self, key: int) -> None:
        if key in self.dictdd:
            del self.dictdd[key] 
            
    def contains(self, key: int) -> bool:
        return key in self.dictdd


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)