import math
from objects.object3D import Object3D
from utils.vector import Vector
from typing import Tuple

class Sphere(Object3D):
    def __init__(self, center: Vector, radius: float, color: Tuple[int]) -> Tuple[float]:
        super().__init__(center, color)
        self.r: float = radius
    
    def __repr__(self) -> str:
        return f"Sphere(c: ({self.center.x}, {self.center.y}, {self.center.z}), r: {self.r}, color: {self.color})"
    
    def intersect(self, O, D):
        r = self.r
        CO = O - self.center
        
        a = D.dot(D) # = 1 because D is normalized
        b = 2 * CO.dot(D)
        c = CO.dot(CO) - r * r
        
        delta = b * b - 4 * a * c
        if delta < 0:
            return math.inf, math.inf
        t1 = (-b + delta**0.5) / 2
        t2 = (-b - delta**0.5) / 2
        return t1, t2