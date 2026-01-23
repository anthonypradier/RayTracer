from abc import abstractmethod
from utils.vector import Vector
from typing import Tuple

class Object3D:
    def __init__(self, center: Vector, color: Tuple[int], specular: int):
        self.center: Vector = center
        self.color: Tuple[int] = color
        self.specular: int = specular
    
    @abstractmethod
    def intersect(self, O: Vector, D: Vector):
        raise "Not implemented method error"