import math
from typing import List, Tuple
from utils.vector import Vector
from objects.sphere import Sphere
from objects.object3D import Object3D

class Scene:
    def __init__(self):
        self.objects: List[Object3D] = []
        self.lights: List = []
        self.bg: tuple = (0, 0, 0)
        
    def initScene(self):
        # self.addSphere(Vector(0, -1, 3), 1.0, (255, 0, 0))
        # self.addSphere(Vector(2, 0, 4), 1.0, (0, 0, 255))
        # self.addSphere(Vector(-2, 0, 4), 1.0, (0, 255, 0))
        self.addSphere(Vector(3, 1, 6), 2.0, (0, 255, 0))
        print("Scene initialized")
        
    def addSphere(self, center: Vector, radius: float, color: Tuple[int]):
        s = Sphere(center, radius, color)
        self.objects.append(s)
        print("Sphere added to scene : " + str(s))
        
    def traceRay(self, O: Vector, D: Vector, t_min: float = 1.0, t_max: float = math.inf) -> Tuple[int]:
        closest_t: float = math.inf
        closest_obj: Object3D = None
        for obj in self.objects:
            t1, t2 = obj.intersect(O, D)
            if t_min <= t1 < t_max and t1 < closest_t:
                closest_t = t1
                closest_obj = obj
            if t_min <= t2 < t_max and t2 < closest_t:
                closest_t = t2
                closest_obj = obj
        if closest_obj == None:
            return self.bg
        return closest_obj.color