from abc import abstractmethod
from utils.vector import Vector

class Object3D:
    def __init__(self, center: Vector):
        self.center: Vector = center
    
    @abstractmethod
    def intersect(self, O: Vector, D: Vector):
        raise "Not implemented method error"