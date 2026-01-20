import math
from utils.vector import Vector

class Scene:
    def __init__(self):
        self.objects = []
        self.lights = []
        self.bg = (0, 0, 0)
        
    def traceRay(self, O: Vector, D: Vector):
        closest_t = math.inf
        closest_obj = None
        for obj in self.objects:
            pass