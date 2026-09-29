class point3D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class point3DSlots:
    __slots__ = {"x", "y"}
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = point3D(2,3)
p.z = 100
print(p.x, p.y, p.z)

p1 = point3DSlots(4, 5)
p1.z = 200
print(p1.x, p1.y, p1.z)