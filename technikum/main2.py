
class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{vars(self)}'

    def __sub__(self, scalar: float):
        return Vector(self. x -scalar, self. y -scalar, self. z -scalar)

    def __rsub__(self, scalar: float):
        return Vector(scalar -self.x, scalar -self.y, scalar -self.z)

    def __mul__(self, other: int):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: int):
        return Vector(self.x / other, self.y / other, self.z / other)

    def __rtruediv__(self, other: int):
        return Vector(other / self.x, other / self.y, other / self.z)


if __name__ =='__main__':
    v1 = Vector(2, 2, 2)
    print(v1 - 1)  # lsub
    print(1 - v1)  # rsub
    print(v1 * 5)  # mul
    print(v1 /3)
    print(5/ v1)
    print(v1.__dict__)