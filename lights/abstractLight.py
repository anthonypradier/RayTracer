from abc import abstractmethod
from utils.vector import Vector

class AbstractLight:
    def __init__(self, intensity: float = 0.0, is_ambient: bool = False):
        self.intensity: float = intensity
        self.is_ambient: bool = is_ambient
        
    @abstractmethod
    def compute_lighting(self, point: Vector) -> float:
        """Calculates the total intensity of light received at the specified point

        Args:
            point (Vector): a point in the scene

        Returns:
            float: the intensity of light
        """
        raise NotImplementedError("get_intensity_at_point need to be implemented")
    
    @abstractmethod
    def get_color_at_point(self, point: Vector) -> tuple:
        """Calculates the color of the point in the scene

        Args:
            point (Vector): a point in the scene
        
        Returns:
            tuple: the color calculated
        """
        raise NotImplementedError("get_color_at_point need to be implemented")
    
    @abstractmethod
    def get_color_at_point(self, point: Vector) -> tuple:
        """Calculates the color of the point in the scene

        Args:
            point (Vector): a point in the scene
        
        Returns:
            tuple: the color calculated
        """
        raise NotImplementedError("get_color_at_point need to be implemented")
    
    @abstractmethod
    def get_intensity_at_point(self, point: Vector, normal: Vector, V: Vector, s: int) -> float:
        """Calculates the intensity of light at the point

        Args:
            point (Vector): a point in the scene
            normal (Vector): the normal of the light ray at the point

        Returns:
            Vector: the intensity of light
        """
        raise NotImplementedError("get_intensity_at_point need to be implemented")