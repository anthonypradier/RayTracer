from lights.abstractLight import AbstractLight
from utils.vector import Vector
from core.scene import *

class PointLight(AbstractLight):
    def __init__(self, intensity: float, position: Vector):
        super().__init__(intensity, False)
        self.position: Vector = position
    
    def __repr__(self):
        return f"PointLight(intensity: {self.intensity}, position: {self.position})"
    
    def get_direction(self) -> Vector:
        return None
    
    def get_position(self) -> Vector:
        return self.position
    
    def compute_lighting(self, point: Vector) -> float:
        return super().compute_lighting(point)
    
    def get_color_at_point(self, point: Vector) -> tuple:
        return super().get_color_at_point(point)
    
    def get_direction_from_point(self, point: Vector) -> Vector:
        return self.position - point
    
    def get_intensity_at_point(self, point, normal, V: Vector, s: int, scene):
        i: float = 0
        direction = self.get_direction_from_point(point)
        n_dot_l = direction.dot(normal)
        t_max = 1.0
         # shadow
        shadow_sphere, shadow_t = scene.closest_intesrsection(point, direction, 1, t_max)
        if shadow_sphere != None:
            return i
        # diffuse
        if n_dot_l > 0:
            i += self.intensity * n_dot_l / (normal.length() * direction.length())
        # specular
        if s != -1:
            R: Vector = normal * 2 * normal.dot(direction) - direction
            r_dot_v = R.dot(V)
            if r_dot_v > 0:
                i += self.intensity * (r_dot_v / (R.length() * normal.length()))**s
        return i