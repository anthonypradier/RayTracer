from lights.abstractLight import AbstractLight
from utils.vector import Vector

class DirLight(AbstractLight):
    def __init__(self, intensity: float, direction: Vector):
        super().__init__(intensity, False)
        self.direction: Vector = direction
    
    def __repr__(self):
        return f"DirLight(intensity: {self.intensity}, direction: {self.direction})"
    
    def get_direction(self) -> Vector:
        return self.direction
    
    def get_position(self) -> Vector:
        return None
    
    def compute_lighting(self, point: Vector) -> float:
        return super().compute_lighting(point)
    
    def get_color_at_point(self, point: Vector) -> tuple:
        return super().get_color_at_point(point)
    
    def get_direction_from_point(self, point: Vector) -> Vector:
        return self.direction
    
    def get_intensity_at_point(self, point: Vector, normal: Vector, V: Vector, s: int):
        direction: Vector = self.direction
        i: float = 0
        n_dot_l = direction.dot(normal)
        if n_dot_l > 0:
            i += self.intensity * n_dot_l / (normal.length() * direction.length())
        if s != -1:
            R: Vector = normal * 2 * normal.dot(direction) - direction
            r_dot_v = R.dot(V)
            if r_dot_v > 0:
                i += self.intensity * (r_dot_v / (R.length() * normal.length()))**s
        return i