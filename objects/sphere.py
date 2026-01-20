from objects import Object3D
from utils.vector import Vector

class Sphere(Object3D):
    def __init__(self, center: Vector, radius: float, color: tuple):
        super(center).__init__()
        self.r: float = radius
        self.color: tuple = color