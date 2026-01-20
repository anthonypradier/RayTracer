from __future__ import annotations

class Vector:
    def __init__(self, x: int | float = 0.0, y: int | float = 0.0, z: int | float = 0.0):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self) -> str:
        return f"Vector(x: {self.x}, y: {self.y}, z: {self.z})"
        
    def __add__(self, v: Vector | int | float) -> Vector:
        if(type(v) == int or type(v) == float):
            return Vector(self.x + v, self.y + v, self.z + v)
        if(isinstance(v, Vector)):
            return Vector(self.x + v.x, self.y + v.y, self.z + v.z)
        print("Uncompatible types for addition")
        return self
        
    def __sub__(self, v: Vector | int | float) -> Vector:
        if(type(v) == int or type(v) == float):
            return Vector(self.x - v, self.y - v, self.z - v)
        if(isinstance(v, Vector)):
            return Vector(self.x - v.x, self.y - v.y, self.z - v.z)
        print("Uncompatible types for substraction")
        return self
        
    def __mul__(self, v: Vector | int | float) -> Vector:
        if(type(v) == int or type(v) == float):
            return Vector(self.x * v, self.y * v, self.z * v)
        if(isinstance(v, Vector)):
            return Vector(self.y * v.z - self.z * v.y, self.z * v.x - self.x * v.z, self.x * v.y - self.y * v.x)
        print("Uncompatible types for cross product")
        return self
    
    def __neg__(self) -> Vector:
        return Vector(-self.x, -self.y, -self.z)
    
    def dot(self, v: Vector) -> int | float:
        return self.x * v.x + self.y * v.y + self.z * v.z
    
    def cross(self, v: Vector) -> int | float:
        return Vector(self.y * v.z - self.z * v.y, self.z * v.x - self.x * v.z, self.x * v.y - self.y * v.x)
    
    def length(self) -> int | float:
        return self.dot(self)**0.5
    
    def normalize(self) -> Vector:
        l = self.length()
        if l == 0:
            return Vector(0, 0, 0)
        return Vector(self.x / l, self.y / l, self.z / l)