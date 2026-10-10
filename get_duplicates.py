class Duplicate:

    def __init__(self, nums):
        self. nums = nums

    def get_unique(self):
        return set(self.nums)
    
    def get_duplicates(self):
        seen = set()
        duplicates = set(x for x in self.nums if x in seen or seen.add(x))
        return duplicates


d = Duplicate([1,1,2,3,4,1,2])
print(d.get_unique())
print(d.get_duplicates())
