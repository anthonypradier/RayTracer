from lights.abstractLight import AbstractLight
from utils.vector import Vector

class PointLight(AbstractLight):
    def __init__(self, intensity: float, position: Vector):
        super().__init__(intensity, False)
        self.position: Vector = position
    
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