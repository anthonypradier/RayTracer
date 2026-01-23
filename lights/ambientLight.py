from lights.abstractLight import AbstractLight
from utils.vector import Vector

class AmbientLight(AbstractLight):
    def __init__(self, intensity: float):
        super().__init__(intensity, True)
        
    def __repr__(self):
        return f"AmbientLight(intensity: {self.intensity})"
    
    def get_direction(self) -> Vector:
        return None
    
    def get_position(self) -> Vector:
        return None
    
    def compute_lighting(self, point: Vector) -> float:
        return super().compute_lighting(point)
    
    def get_color_at_point(self, point: Vector) -> tuple:
        return super().get_color_at_point(point)
    
    def get_direction_from_point(self, point: Vector) -> Vector:
        return None
    
    def get_intensity_at_point(self, point: Vector, normal: Vector, V: Vector, s: int, scene):
        return self.intensity